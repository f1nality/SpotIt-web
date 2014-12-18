from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from push_notifications.gcm import GCMError
from push_notifications.models import GCMDevice
from application import settings
from rest_framework.authtoken.models import Token
from spotit.models import PostUserRating, PostCommentUserRating, PostComment, Post


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=Post)
def post_post_save(sender, **kwargs):
    if kwargs.get('created'):
        post = kwargs.get('instance')

        devices_ids = GCMDevice.objects.values('user', 'device_id', 'registration_id').distinct().values('pk').all()
        devices = GCMDevice.objects.filter(pk__in=devices_ids).all()

        try:
            devices.send_message('post_save', extra={
                'post_id': post.pk,
                'post_author_id': post.author,
                'post_text': post.text,
                'post_date_add': str(post.date_add),
                'post_author_ip': post.author_ip,
                'post_rating': post.rating,
                'post_count_vote': post.count_vote,
                'post_count_comments': post.count_comments,
                'post_latitude': post.count_comments,
                'post_longitude': post.count_comments,
            })
        except GCMError:
            pass


@receiver(post_save, sender=PostComment)
def post_comment_post_save(sender, **kwargs):
    if kwargs.get('created'):
        post_comment = kwargs.get('instance')

        post_comment.post.count_comments += 1
        post_comment.post.save()

        if post_comment.author != post_comment.post.author:
            devices_ids = GCMDevice.objects.values('user', 'device_id', 'registration_id').distinct().filter(
                user__pk=post_comment.post.author.pk
            ).values('pk').all()

            devices = GCMDevice.objects.filter(pk__in=devices_ids).all()

            try:
                devices.send_message('new_answer_comment', extra={
                    'post_id': post_comment.post.pk,
                    'post_comment_id': post_comment.pk,
                    'post_comment_text': post_comment.text,
                    'post_comment_author_id': post_comment.author.pk,
                    'post_comment_author_name': unicode(post_comment.author),
                })
            except GCMError:
                pass

@receiver(post_delete, sender=PostComment)
def post_comment_delete(sender, **kwargs):
    post_comment = kwargs.get('instance')

    post_comment.post.count_comments -= 1
    post_comment.post.save()


@receiver(post_save, sender=PostUserRating)
def post_user_rating_post_save(sender, **kwargs):
    if kwargs.get('created'):
        post_user_rating = kwargs.get('instance')

        post_user_rating.post.rating += post_user_rating.vote
        post_user_rating.post.count_vote += 1
        post_user_rating.post.save()


@receiver(post_delete, sender=PostUserRating)
def post_user_rating_post_delete(sender, **kwargs):
    post_user_rating = kwargs.get('instance')

    post_user_rating.post.rating -= post_user_rating.vote
    post_user_rating.post.count_vote -= 1
    post_user_rating.post.save()
    
    
@receiver(post_save, sender=PostCommentUserRating)
def post_comment_user_rating_post_save(sender, **kwargs):
    if kwargs.get('created'):
        post_comment_user_rating = kwargs.get('instance')

        post_comment_user_rating.post.rating += post_comment_user_rating.vote
        post_comment_user_rating.post.count_vote += 1
        post_comment_user_rating.post.save()


@receiver(post_delete, sender=PostCommentUserRating)
def post_comment_user_rating_post_delete(sender, **kwargs):
    post_comment_user_rating = kwargs.get('instance')

    post_comment_user_rating.post.rating -= post_comment_user_rating.vote
    post_comment_user_rating.post.count_vote -= 1
    post_comment_user_rating.post.save()
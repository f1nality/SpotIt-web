from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from push_notifications.gcm import GCMError
from push_notifications.models import GCMDevice
from application import settings
from rest_framework.authtoken.models import Token
from spotit.models import PostUserRating, PostCommentUserRating, PostComment


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=PostComment)
def post_comment_post_save(sender, **kwargs):
    if kwargs.get('created'):
        post_comment = kwargs.get('instance')

        if post_comment.author != post_comment.post.author:
            devices = GCMDevice.objects.filter(user__pk=post_comment.post.author.pk).all()

            try:
                devices.send_message(post_comment.text, extra={
                    'post_id': post_comment.post.pk,
                    'post_comment_id': post_comment.pk,
                    'post_comment_author_id': post_comment.author.pk,
                    'post_comment_author_name': post_comment.author,
                })
            except GCMError:
                pass


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
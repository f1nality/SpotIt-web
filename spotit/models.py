# encoding: utf-8
from django.db import models
from django.utils import timezone
from core.models import User


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name=u'Автор', related_name='posts')
    text = models.TextField(verbose_name=u'Текст')
    date_add = models.DateTimeField(verbose_name=u'Дата создания', default=timezone.now)
    author_ip = models.CharField(max_length=255, verbose_name=u'IP автора')
    rating = models.FloatField(default=0, verbose_name=u'Рейтинг')
    count_vote = models.IntegerField(default=0, verbose_name=u'Количество проголосоваваших')
    count_comments = models.IntegerField(default=0, verbose_name=u'Количество комментариев')
    latitude = models.FloatField(verbose_name=u'Широта')
    longitude = models.FloatField(verbose_name=u'Долгота')

    class Meta:
        verbose_name = u'пост'
        verbose_name_plural = u'посты'
        ordering = ['-date_add']

    def __unicode__(self):
        return u'Пост {0}'.format(
            self.author
        )


class PostPhoto(models.Model):
    post = models.ForeignKey(Post, verbose_name=u'Пост', related_name='photos')
    image = models.ImageField(verbose_name=u'Картинка', upload_to='post_photos/')
    date_add = models.DateTimeField(verbose_name=u'Дата создания', default=timezone.now)

    class Meta:
        verbose_name = u'фото поста'
        verbose_name_plural = u'фото постов'
        ordering = ['-date_add']

    def __unicode__(self):
        return u'Фото поста {0}'.format(
            self.post
        )


class PostComment(models.Model):
    post = models.ForeignKey(Post, verbose_name=u'Пост', related_name='comments')
    author = models.ForeignKey(User, verbose_name=u'Автор', related_name='post_comments')
    text = models.TextField(verbose_name=u'Текст')
    date_add = models.DateTimeField(verbose_name=u'Дата создания', default=timezone.now)
    author_ip = models.CharField(max_length=255, verbose_name=u'IP автора')
    rating = models.FloatField(default=0, verbose_name=u'Рейтинг')
    count_vote = models.IntegerField(default=0, verbose_name=u'Количество проголосоваваших')
    deleted = models.BooleanField(default=False, verbose_name=u'Удален')
    latitude = models.FloatField(verbose_name=u'Широта')
    longitude = models.FloatField(verbose_name=u'Долгота')

    class Meta:
        verbose_name = u'комментарий'
        verbose_name_plural = u'комментарии'
        ordering = ['date_add']

    def __unicode__(self):
        return u'Комментарий {0} за {1}'.format(
            self.author,
            self.date_add
        )

    def get_user_vote(self, user):
        rating = self.ratings.filter(user=user).first()
        if rating:
            return rating.vote
        else:
            return None


class PostUserRating(models.Model):
    post = models.ForeignKey(Post, verbose_name=u'Пост', related_name='ratings')
    user = models.ForeignKey(User, verbose_name=u'Автор', related_name='post_ratings')
    vote = models.IntegerField(verbose_name=u'Изменение рейтинга')
    date = models.DateTimeField(verbose_name=u'Дата', default=timezone.now)

    class Meta:
        verbose_name = u'рейтинг поста'
        verbose_name_plural = u'рейтинги постов'

    def __unicode__(self):
        return u'Рейтинг {0} пользователя {1}'.format(
            self.post,
            self.user
        )


class PostCommentUserRating(models.Model):
    post_comment = models.ForeignKey(PostComment, verbose_name=u'Пост', related_name='ratings')
    user = models.ForeignKey(User, verbose_name=u'Автор', related_name='post_comment_ratings')
    vote = models.IntegerField(verbose_name=u'Изменение рейтинга')
    date = models.DateTimeField(verbose_name=u'Дата', default=timezone.now)

    class Meta:
        verbose_name = u'рейтинг комментария'
        verbose_name_plural = u'рейтинги комментариев'

    def __unicode__(self):
        return u'Рейтинг {0} пользователя {1}'.format(
            self.post_comment,
            self.user
        )


from spotit import signals
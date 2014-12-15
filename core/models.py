# encoding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    SEX_CHOICES = (
        ('m', u'Мужской'),
        ('f', u'Женский'),
    )

    date_of_birth = models.DateField(blank=True, null=True, verbose_name=u'Дата рождения')
    sex = models.CharField(blank=True, null=True, max_length=1, verbose_name=u'Пол', choices=SEX_CHOICES)
    phone_number = models.CharField(blank=True, null=True, verbose_name=u'Телефон', max_length=255)
    photo = models.ImageField(verbose_name=u'', upload_to='user_photos/', null=True, blank=True, default=None)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        unique_together = (
            ('email',),
            ('phone_number',),
        )

    def __unicode__(self):
        if self.first_name:
            return self.first_name + ' ' + self.last_name
        return self.email
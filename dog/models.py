from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
from accounts.models import User


class Mission(models.Model):
    title = models.CharField(max_length=220, null=True, blank=True)
    en_title = models.CharField(max_length=220, null=True, blank=True)
    summary = models.CharField(max_length=220,    verbose_name='요약', null=True, blank=True)

    class Level(models.IntegerChoices):
        very_easy = 1
        easy = 2
        normal = 3
        difficult = 4
        very_difficult = 5

    level = models.IntegerField(choices=Level.choices, null=True, blank=True)
    description = models.TextField(blank=True,  verbose_name='미션 설명',null=True)
    profile_img = models.ImageField(
        upload_to="profile_img",
        null=True,
        blank=True,
        verbose_name='프로필 이미지'
    )
    materials = models.CharField(max_length=220,  verbose_name='준비물', null=True, blank=True)
    created = models.DateTimeField(auto_created=True)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Community(models.Model):
    title = models.CharField(max_length=220, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    create = models.DateField(null=True, auto_created=True)
    img = models.ImageField(
        upload_to="img/",
        null=True,
        blank=True,
        verbose_name='이미지 첨부',
        default=''
    )
    counting = models.PositiveIntegerField(default=0, verbose_name='조회수')

    def __str__(self):
        return self.title


class SaveIp(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    access_ip = models.CharField(max_length=20, null=True, blank=True)


class Life(models.Model):
    title = models.CharField(max_length=220, null=True, blank=True)
    en_title = models.CharField(max_length=220, null=True, blank=True)
    img = models.ImageField(
        upload_to="img/",
        null=True,
        blank=True,
        verbose_name='이미지 첨부',
        default=''
    )
    summary = models.CharField(max_length=220,    verbose_name='요약', null=True, blank=True)
    materials = models.CharField(max_length=220,  verbose_name='준비물', null=True, blank=True)
    created = models.DateTimeField(auto_created=True)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title

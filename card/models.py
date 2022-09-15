from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
from accounts.models import User


class Card(models.Model):
    name = models.TextField(
        null=True,
        blank=True,
        verbose_name='이름'
    )
    name_color = models.TextField(
        null=True,
        blank=True,
        verbose_name='이름 색'

    )
    content1 = models.TextField(
        null=True,
        blank=True,
        verbose_name='담당업무'
    )
    content1_color = models.TextField(
        null=True,
        blank=True,
        verbose_name='담당업무 색'
    )
    content2 = models.TextField(
        null=True,
        blank=True,
        verbose_name='기타업무'
    )
    content2_color = models.TextField(
        null=True,
        blank=True,
        verbose_name='기타업무 색'
    )
    business_name = models.TextField(
        null=True,
        blank=True,
        verbose_name='회사 명'
    )
    business_name_color = models.TextField(
        null=True,
        blank=True,
        verbose_name='회사 명 색'
    )
    profile_img = models.ImageField(
        upload_to="profile_img",
        null=True,
        blank=True,
        verbose_name='프로필 이미지'
    )
    background_color = models.TextField(
        null=True,
        blank=True,
        verbose_name='배경색'
    )

    def __str__(self):
        return self.name


class Meta:
    db_table = 'card_info'
    verbose_name = '명함'
    verbose_name_plural = '명함'

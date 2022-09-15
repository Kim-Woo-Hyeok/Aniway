from django.conf import settings
from django.db import models
from django.utils import timezone
from accounts.models import User


class Feed(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='유저'
    )
    content = models.TextField(
        null=True,
        blank=True,
        verbose_name='내용'
    )
    img = models.ImageField(
        upload_to='uploads/feeds/%Y/%m/%d',
        null=True,
        blank=True,
        verbose_name='이미지'
    )
    profile_imge = models.ImageField(
        upload_to='uploads/feeds/%Y/%m/%d',
        null=True,
        blank=True,
        verbose_name='프로필 이미지'
    )
    like_count = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='좋아요 수'
    )
    name = models.CharField(
        max_length=200,
        null=True,
    )


    def __str__(self):
        return self.user.email

    class Meta:
        db_table = 'feeds'
        verbose_name = '피드'
        verbose_name_plural = '피드'


class FeedLike(models.Model):
    feed = models.ForeignKey(
        Feed,
        on_delete=models.CASCADE,
        verbose_name='피드'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='좋아요한 유저'
    )

    def __str__(self):
        return self.feed.user.email

    class Meta:
        db_table = 'feed_like'
        verbose_name = '피드 좋아요'
        verbose_name_plural = '피드 좋아요'

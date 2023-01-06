from django.conf import settings
from django.db import models
from django.utils import timezone
from accounts.models import User


class Community(models.Model):
    title = models.CharField(max_length=220, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    create = models.DateField(null=True, auto_created=True,)
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
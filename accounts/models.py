from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from accounts.managers import UserManager
from datetime import date, datetime
import datetime


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
        null=True,
        default=True
    )
    name = models.CharField(
        verbose_name='name',
        max_length=255,
        default='',
        null=True
    )

    GENDER_MAN = "M"
    GENDER_WOMAN = "W"
    GENDER_CHOICES = ((GENDER_MAN, "남"), (GENDER_WOMAN, "여"))

    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=2, null=True, blank=True
    )

    phone = models.CharField(
        verbose_name='phone',
        max_length=255,
        default='',
        null=True
    )

    date_of_birth = models.DateField()

    pet_name = models.CharField(
        verbose_name='pet_name',
        max_length=255,
        default='',
        null=True
    )

    pet_MAN = "PET_M"
    pet_WOMAN = "PET_W"
    PET_CHOICES = ((GENDER_MAN, "수컷"), (GENDER_WOMAN, "암컷"))

    pet_gender = models.CharField(
        choices=PET_CHOICES, max_length=2, null=True, blank=True
    )

    pet_breed = models.CharField(
        verbose_name='pet_breed',
        max_length=255,
        null=True,
        default=''
    )

    pet_weight = models.CharField(
        verbose_name='pet_weight',
        max_length=255,
        null=True,
        default=''
    )

    YES = "YES"
    NO = "NO"
    neuter_choices = ((YES, "여"), (NO, "부"))

    pet_neuter = models.CharField(
        choices=neuter_choices, max_length=20, null=True, blank=True
    )

    pet_date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['date_of_birth', 'name']

    def get_age(self):
        today = date.today()
        birth = self.pet_date_of_birth
        return today.year - birth.year + 1
# (Custom User Model)을 기본 유저 모델(Model)로 사용하기 위해

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


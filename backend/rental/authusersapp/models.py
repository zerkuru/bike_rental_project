from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
# Логин
# Пароль
# ФИО
# Адрес
# Телефон
# Статус на сайте


class UsersModel(AbstractUser):
    full_name = models.CharField(_('first name'), max_length=30, blank=True)
    address = models.TextField(max_length=100, blank=True)
    tel_number = models.CharField(max_length=11, blank=True)
    is_staff = models.BooleanField(_('active'), default=False)
    is_activated = models.BooleanField(_('active'), default=True)
    email = models.EmailField(_('email address'), unique=True)

    REQUIRED_FIELDS = ['email', 'full_name', 'address', 'tel_number' , 'is_staff']


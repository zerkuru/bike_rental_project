from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import CASCADE

from authusersapp.models import UsersModel
from transportapp.models import TransportModel


class Review(models.Model):
    author = models.ForeignKey(
        UsersModel,
        on_delete=CASCADE,
        verbose_name='автор'
    )

    transport = models.ForeignKey(
        TransportModel,
        on_delete=CASCADE,
        verbose_name='транспорт')

    review_text = models.TextField(
        verbose_name='содержание',
        blank=True,
    )

    score = models.PositiveSmallIntegerField(
        default=0,
        blank=True,
        null=True,
        verbose_name='оценка',
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    created_at = models.DateField(
        verbose_name='создан',
        auto_now_add=True
    )

    updated_at = models.DateField(
        verbose_name='изменен',
        auto_now=True
    )

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

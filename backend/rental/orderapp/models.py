from django.db import models
from django.db.models import CASCADE, Q
from django.utils.timezone import now

from authusersapp.models import UsersModel
from transportapp.models import TransportModel


class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_OWNER = 'STP'
    READY = 'RDY'
    CANCEL = 'CNC'
    FINISHED = 'FSD'

    ORDER_STATUS = (
        (FORMING, 'формируется'),
        (SENT_TO_OWNER, 'отправлен владельцу ТС'),
        (READY, 'подтвержден'),
        (CANCEL, 'отменен'),
        (FINISHED, 'завершен'),
    )

    user = models.ForeignKey(
        UsersModel,
        on_delete=CASCADE)

    transport = models.ForeignKey(
        TransportModel,
        on_delete=CASCADE)

    date_from = models.DateTimeField(
        verbose_name='время начала аренды',
    )

    date_to = models.DateTimeField(
        verbose_name='время окончания аренды',
    )

    conditions = models.TextField(
        verbose_name='условия аренды',
        max_length=300)

    status = models.CharField(
        verbose_name='статус',
        max_length=3,
        choices=ORDER_STATUS,
        default=FORMING
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

    def __str__(self):
        return f'Заказ {self.user.username} №{self.id} от {self.created_at}'




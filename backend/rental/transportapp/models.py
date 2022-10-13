from django.db import models

from authusersapp.models import UsersModel


class TransportTypeModel(models.Model):
    class Meta:
        verbose_name = 'тип транспорта'
        verbose_name_plural = 'тип транспорта'

    name = models.CharField(
        verbose_name='тип',
        max_length=30)

    def __str__(self):
        return self.name
    
    
class ManufacturerModel(models.Model):
    class Meta:
        verbose_name = 'производитель'
        verbose_name_plural = 'производитель'

    name = models.CharField(
        verbose_name='производитель',
        max_length=30)

    def __str__(self):
        return self.name


class TransportModel(models.Model):

    transport_type = models.ForeignKey(
        TransportTypeModel,
        verbose_name='тип',
        on_delete=models.CASCADE,
        default=None)

    manufacturer = models.ForeignKey(
        ManufacturerModel,
        verbose_name='производитель',
        on_delete=models.CASCADE,
        default=None)

    transport_model = models.CharField(
        verbose_name='модель',
        max_length=30,
        blank=True)

    year = models.CharField(
        verbose_name='год производства',
        max_length=30,
        blank=True)

    transport_owner = models.ForeignKey(
        UsersModel,
        verbose_name='владелец',
        on_delete=models.CASCADE)

    age_limit = models.PositiveIntegerField(
        verbose_name='возрастное ограничение',
        null=True,
        blank=True)

    information = models.TextField(
        verbose_name='информация',
        max_length=500,
        blank=True)

    rental_price = models.PositiveIntegerField(
        verbose_name='стоимость аренды',
        blank=True)

    deposit = models.PositiveIntegerField(
        verbose_name='сумма залога',
        blank=True,
        null=True)

    image = models.ImageField(
        verbose_name='изображение',
        blank=True,
        upload_to='imgTransport/',
    )

    def __str__(self):
        return f'{self.transport_type} - {self.transport_model}'

    class Meta:
        verbose_name = 'транспорт'
        verbose_name_plural = 'транспорт'









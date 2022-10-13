# Generated by Django 4.0.5 on 2022-07-28 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transportapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateTimeField(verbose_name='время начала аренды')),
                ('date_to', models.DateTimeField(verbose_name='время окончания аренды')),
                ('conditions', models.TextField(max_length=300, verbose_name='условия аренды')),
                ('status', models.CharField(choices=[('FM', 'формируется'), ('STP', 'отправлен владельцу ТС'), ('RDY', 'подтвержден'), ('CNC', 'отменен'), ('FSD', 'завершен')], default='FM', max_length=3, verbose_name='статус')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='создан')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='изменен')),
                ('transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transportapp.transportmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
                'ordering': ('-created_at',),
            },
        ),
    ]
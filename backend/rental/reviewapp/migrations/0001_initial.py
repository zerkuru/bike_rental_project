# Generated by Django 4.0.5 on 2022-07-22 16:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transportapp', '0004_alter_transportmodel_deposit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField(blank=True, verbose_name='содержание')),
                ('score', models.PositiveSmallIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='оценка')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='создан')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='изменен')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
                ('transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transportapp.transportmodel', verbose_name='транспорт')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
                'ordering': ('-created_at',),
            },
        ),
    ]

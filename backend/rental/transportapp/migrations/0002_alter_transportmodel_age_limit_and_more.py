# Generated by Django 4.0.6 on 2022-07-17 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportmodel',
            name='age_limit',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='возрастное ограничение'),
        ),
        migrations.AlterField(
            model_name='transportmodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='imgTransport', verbose_name='изображение'),
        ),
    ]

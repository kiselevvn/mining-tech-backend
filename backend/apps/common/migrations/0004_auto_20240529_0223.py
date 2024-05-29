# Generated by Django 3.2.25 on 2024-05-28 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='type',
            field=models.CharField(choices=[('phone', 'Телефон'), ('email', 'Электронный адрес'), ('vk', 'Вконтакте'), ('tg', 'Телеграм'), ('link', 'Ссылка')], max_length=50, verbose_name='Вид'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='value',
            field=models.TextField(verbose_name='Значение'),
        ),
    ]

# Generated by Django 3.2.25 on 2024-06-04 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Адрес', 'verbose_name_plural': 'Адреса'},
        ),
    ]

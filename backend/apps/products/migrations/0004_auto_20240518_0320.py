# Generated by Django 3.2.25 on 2024-05-18 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('products', '0003_auto_20240510_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='algorithm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.algorithm', verbose_name='Алгоритм шифрования'),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.brand', verbose_name='Производитель'),
        ),
        migrations.AddField(
            model_name='product',
            name='currency_mining',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.currencymining', verbose_name='Валюта'),
        ),
        migrations.AddField(
            model_name='product',
            name='hashrate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.hashrate', verbose_name='Хешрейт'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_pre_order',
            field=models.BooleanField(default=False, verbose_name='Доступен предзаказ'),
        ),
        migrations.AddField(
            model_name='product',
            name='power',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.power', verbose_name='Потребление энергии'),
        ),
    ]

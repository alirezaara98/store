# Generated by Django 3.1.4 on 2021-02-16 14:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_orderitems_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='JoinDate'),
        ),
    ]

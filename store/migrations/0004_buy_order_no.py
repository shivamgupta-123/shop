# Generated by Django 3.0.2 on 2020-08-12 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200812_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='order_no',
            field=models.CharField(default='', max_length=10),
        ),
    ]
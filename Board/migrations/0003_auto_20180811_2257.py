# Generated by Django 2.1 on 2018-08-11 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Board', '0002_auto_20180811_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='isOnGifMonitor',
            field=models.BooleanField(default=False, unique=True),
        ),
    ]

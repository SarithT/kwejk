# Generated by Django 2.1 on 2018-08-11 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Board', '0003_auto_20180811_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='isOnGifMonitor',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.2 on 2021-04-23 11:58

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210423_0953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='telegramdata',
            options={'verbose_name': 'Telegram data', 'verbose_name_plural': 'Telegram data'},
        ),
        migrations.AlterField(
            model_name='telegramdata',
            name='token',
            field=models.CharField(max_length=45, unique=True, validators=[core.models.validate_token]),
        ),
    ]

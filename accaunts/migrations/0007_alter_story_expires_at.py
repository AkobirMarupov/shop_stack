# Generated by Django 5.2.1 on 2025-06-22 14:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accaunts', '0006_story_is_active_alter_story_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 23, 14, 6, 12, 547533, tzinfo=datetime.timezone.utc)),
        ),
    ]

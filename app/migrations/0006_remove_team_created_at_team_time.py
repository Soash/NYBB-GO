# Generated by Django 4.0.6 on 2024-04-01 09:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_team_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='created_at',
        ),
        migrations.AddField(
            model_name='team',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 16, 0, tzinfo=utc)),
        ),
    ]
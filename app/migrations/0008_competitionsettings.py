# Generated by Django 4.0.6 on 2024-04-01 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_team_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetitionSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('over_time', models.DateTimeField()),
            ],
        ),
    ]

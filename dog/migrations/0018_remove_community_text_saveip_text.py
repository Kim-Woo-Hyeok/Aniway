# Generated by Django 4.0.4 on 2022-09-27 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0017_alter_mission_profile_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='text',
        ),
        migrations.AddField(
            model_name='saveip',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]

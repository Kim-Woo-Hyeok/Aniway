# Generated by Django 4.0.4 on 2022-08-24 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0007_alter_community_create_alter_community_img_one'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='img_one',
        ),
    ]

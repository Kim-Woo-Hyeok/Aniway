# Generated by Django 4.0.4 on 2023-01-03 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_alter_community_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='create',
            field=models.DateField(auto_created=True, null=True),
        ),
    ]
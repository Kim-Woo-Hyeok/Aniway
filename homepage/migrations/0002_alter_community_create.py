# Generated by Django 4.0.4 on 2023-01-03 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='create',
            field=models.DateTimeField(auto_created=True, null=True),
        ),
    ]
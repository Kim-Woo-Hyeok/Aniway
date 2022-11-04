# Generated by Django 4.0.4 on 2022-08-23 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0005_mission_profile_img_alter_mission_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(blank=True, max_length=220, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('img_one', models.ImageField(blank=True, null=True, upload_to='profile_img', verbose_name='프로필 이미지')),
                ('counting', models.CharField(blank=True, max_length=220, null=True)),
            ],
        ),
    ]
# Generated by Django 4.0.4 on 2022-08-18 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0004_alter_mission_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='profile_img', verbose_name='프로필 이미지'),
        ),
        migrations.AlterField(
            model_name='mission',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='미션 설명'),
        ),
        migrations.AlterField(
            model_name='mission',
            name='materials',
            field=models.CharField(blank=True, max_length=220, null=True, verbose_name='준비물'),
        ),
        migrations.AlterField(
            model_name='mission',
            name='summary',
            field=models.CharField(blank=True, max_length=220, null=True, verbose_name='요약'),
        ),
    ]

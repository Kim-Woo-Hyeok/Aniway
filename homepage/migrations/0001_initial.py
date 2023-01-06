# Generated by Django 4.0.4 on 2023-01-02 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_created=True, null=True)),
                ('title', models.CharField(blank=True, max_length=220, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, default='', null=True, upload_to='img/', verbose_name='이미지 첨부')),
                ('counting', models.PositiveIntegerField(default=0, verbose_name='조회수')),
            ],
        ),
        migrations.CreateModel(
            name='SaveIp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_ip', models.CharField(blank=True, max_length=20, null=True)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.community')),
            ],
        ),
    ]
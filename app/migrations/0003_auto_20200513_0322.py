# Generated by Django 3.0.4 on 2020-05-12 21:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20200513_0257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fps',
            name='user',
        ),
        migrations.AddField(
            model_name='fps',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 3.0.4 on 2020-05-13 01:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20200513_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='rationcard',
            name='phone',
            field=models.TextField(default=9999999999, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fps',
            name='user',
            field=models.ManyToManyField(related_name='set', to=settings.AUTH_USER_MODEL),
        ),
    ]
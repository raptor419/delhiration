# -*- encoding: utf-8 -*-


from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class Circle(models.Model):
    number = models.PositiveSmallIntegerField(primary_key=True, db_index=True)
    name = models.TextField(max_length=128, db_index=True, null=True)

class FPS(models.Model):
    number = models.PositiveSmallIntegerField(primary_key=True, db_index=True)
    name = models.TextField(blank=False, db_index=True)
    address = models.TextField(blank=False)
    user = models.ManyToManyField(User, related_name='FPSs')
    circle = models.ForeignKey('Circle', on_delete=models.CASCADE)

class RationCard(models.Model):
    number = models.CharField(primary_key=True, max_length=12, validators=[RegexValidator(r'^[0][0-9]{11}')], db_index=True)
    number_raw = models.CharField(max_length=12, validators=[RegexValidator(r'^[0][0-9]{11}')], db_index=True)
    headoffamily = models.TextField(max_length=128, blank=False)
    # shop = models.ForeignKey('FPS', on_delete=models.CASCADE)

class Locality(models.Model):
    name = models.TextField(max_length=128, db_index=True)
    number = models.PositiveSmallIntegerField(primary_key=True, db_index=True)
    # circlenumber = models.IntegerField(blank=True)
    circle = models.ForeignKey('Circle', on_delete=models.CASCADE)

class Collection(models.Model):
    benificiary_name = models.TextField(max_length=100, blank=False)
    rationcard_number = models.CharField(max_length=12, validators=[RegexValidator(r'^[0][0-9]{11}')], db_index=True)
    rationcard = models.ForeignKey('RationCard', on_delete=models.CASCADE,blank=True, null=True)
    locality = models.ForeignKey('Locality', on_delete=models.CASCADE)
    fps = models.ForeignKey('FPS', on_delete=models.CASCADE)
    mobile_number =  models.CharField(max_length=10, validators=[RegexValidator(regex='[1-9][0-9]{9}')])
    entry_made_by = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_made_at = models.DateTimeField(auto_now_add=True)



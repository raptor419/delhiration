# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CircleNumber(models.Model):
    circle_number = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    circle_name = models.TextField(max_length=500, blank=True)

class FPShop(models.Model):
    fpshop_number = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    fpshop_name = models.TextField(blank=False)
    fpshop_address = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # circlenumber = models.IntegerField(blank=True)
    circlenumber_key = models.ForeignKey('CircleNumber', on_delete=models.CASCADE)

class RationCard(models.Model):
    rationcard_number = models.CharField(primary_key=True, max_length=12, validators=[RegexValidator(r'^\d{1,10}$')])
    familyhead_name = models.TextField(max_length=100, blank=False)
    shop_name = models.IntegerField(blank=True)
    # shop_key = models.ForeignKey('FPShop', on_delete=models.CASCADE)

class Locality(models.Model):
    locality_name = models.TextField(primary_key=True,max_length=500, blank=False)
    locality_number = models.IntegerField(blank=True)
    # circlenumber = models.IntegerField(blank=True)
    circlenumber_key = models.ForeignKey('CircleNumber', on_delete=models.CASCADE)

class Collection(models.Model):
    collection_id = models.TextField(primary_key=True, max_length=500, blank=False)
    # rationcard_number = models.TextField(max_length=12, blank=False)
    collector_name = models.TextField(max_length=100, blank=True)
    rationcard_key = models.ForeignKey('RationCard', on_delete=models.CASCADE)
    # locality_name = models.TextField(max_length=500, blank=True)
    locality_key = models.ForeignKey('Locality', on_delete=models.CASCADE)
    shop_key = models.IntegerField(blank=True)
    shop_name = models.ForeignKey('FPShop', on_delete=models.CASCADE)
    # locality_name = models.TextField(max_length=500, blank=False)
    locality_key = models.ForeignKey('Locality', on_delete=models.CASCADE)
    mobile_number =  models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    # shopuser = models.TextField(max_length=100, blank=True)
    shopuser_key = models.ForeignKey(User, on_delete=models.CASCADE)

class Ration(models.Model):
    ration_type = models.CharField(max_length=30)
    quantity = models.CharField(max_length=30)


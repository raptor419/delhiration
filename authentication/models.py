# -*- encoding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


mobile_rx_validator = RegexValidator(regex='[1-9][0-9]{9}', message='Please enter a valid 10 digit mobile number')

class User(AbstractUser):
    number = models.CharField(max_length=10,validators=[mobile_rx_validator])
    usertype = models.TextField(default="FPSUser")
    FPScreds = models.BooleanField(default=True)

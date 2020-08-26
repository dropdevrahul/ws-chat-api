# -*- coding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ApiUser(AbstractUser):
    LOGGED_IN = "S"
    LOGGED_OUT = "F"
    LOGGED_CHOICES =(
        (LOGGED_IN, 'Logged In'),
        (LOGGED_OUT, 'Logged Out'),
    )
    logged_status = models.CharField(max_length=1, choices=LOGGED_CHOICES)

from django.db import models

# Create your models here.

class Counter(models.Model):
    id = models.AutoField(primary_key=True)
    count = models.IntegerField(default=0)
    ip_address = models.CharField(max_length=15, default='127.0.0.1')
    os = models.CharField(max_length=10, default='Windows')
    osVersion = models.CharField(max_length=10, default='10')
    browser = models.CharField(max_length=10, default='Chrome')
    browserVersion = models.CharField(max_length=10, default='10')
    device = models.CharField(max_length=10, default='PC')
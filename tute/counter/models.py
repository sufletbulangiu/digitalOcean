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
    session_key = models.CharField(max_length=100, default='8aswqe8e4gzk047017sphpjf36kzt5oc', null=True)

    def __str__(self) :
        return f'Id: {self.id} - Ip Address: {self.ip_address}'
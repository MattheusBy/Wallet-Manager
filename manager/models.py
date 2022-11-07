from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    location = models.CharField(max_length=30, blank=True)
    balance = models.FloatField(default=0)

    def __str__(self):
        return f' {self.user}'


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    amount = models.FloatField(default=0)
    time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default='1')
    organization = models.CharField(max_length=512, blank=True)
    description = models.CharField(max_length=2056,blank=True)
    profit = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} {self.amount} {self.category}'


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

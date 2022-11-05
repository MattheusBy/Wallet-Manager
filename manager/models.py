from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

token = Token.objects.create(user=...)
print(token.key)

# Создайте свои модели здесь.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    token = Token.objects.create(user=...)
    def __str__(self):
        return self.user.username

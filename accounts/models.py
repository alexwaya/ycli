from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    org_name     = models.CharField(max_length=30, default="Organization", help_text='Organization Name.')
    categories 			  = models.CharField(max_length=20, default="Kitui")
    date_joined           = models.DateTimeField(verbose_name="date Joined", auto_now_add=True)

    def __str__(self):
        return self.org_name


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
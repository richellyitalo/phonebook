from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return self.name + ' - ' + self.phonenumber

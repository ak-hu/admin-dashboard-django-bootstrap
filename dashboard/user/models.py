from django.db import models


class Main(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=50)
    country = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


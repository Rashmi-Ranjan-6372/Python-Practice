from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=10)
    middle_name = models.CharField(max_length=10, blank = True)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=200, unique = True)
    mobile = models.CharField(max_length=10, unique = True)
    address = models.TextField(max_length=100)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.first_name + " " + self.last_name

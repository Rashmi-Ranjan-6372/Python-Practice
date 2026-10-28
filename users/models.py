from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = None

    first_name = models.CharField(max_length=10)
    middle_name = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=200, unique = True)
    mobile = models.CharField(max_length=10, unique = True)
    address = models.TextField(max_length=100)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["first_name", "last_name", "mobile"]

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}".strip()
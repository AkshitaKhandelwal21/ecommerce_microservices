from django.db import models
from django.contrib.auth.models import AbstractUser

from auths.managers import CustomUserManager

 
# Create your models here.
class Users(AbstractUser):
    RoleChoices = (
        ("customer", "Customer"),
        ("seller", "Seller"),
        ("admin", "Admin"),
    )

    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    roles = models.JSONField(choices=RoleChoices, default="customer")
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def has_role(self, role):
        return role in self.roles
    
    def add_role(self, role):
        if role not in self.roles:
            self.roles.append(role)
            self.save()

    def remove_role(self, role):
        if role in self.roles:
            self.roles.remove(role)
            self.save()

    
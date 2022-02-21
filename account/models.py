from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_administrator = models.BooleanField(default=True)


class AdministratorProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='administrator_profile')

    def __str__(self):
        return f"Profile for {self.user.username}"


class PharmacistProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='pharmacist_profile')

    def __str__(self):
        return f"Profile for {self.user.username}"

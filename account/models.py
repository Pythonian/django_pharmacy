from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_administrator = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)


class Administrator(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='administrator')

    def __str__(self):
        return f"Profile for {self.user.username}"


class Employee(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='employee')
    name = models.CharField(max_length=255, blank=True, null=True)
    joined_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    bank_account_no = models.CharField(max_length=255, blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}"


class EmployeeSalary(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='salaries')
    salary_date = models.DateField()
    salary_amount = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Employee Salaries'

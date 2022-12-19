from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee, Administrator, User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_administrator:
            Administrator.objects.create(user=instance)
        if instance.is_employee:
            Employee.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_administrator:
        instance.administrator.save()
    if instance.is_employee:
        instance.employee.save()

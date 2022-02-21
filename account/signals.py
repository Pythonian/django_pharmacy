from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PharmacistProfile, AdministratorProfile, User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.is_administrator:
        AdministratorProfile.objects.get_or_create(user=instance)
    else:
        PharmacistProfile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_administrator:
        instance.administrator_profile.save()
    else:
        PharmacistProfile.objects.get_or_create(user=instance)

from django.db.models.signals import post_save  # The signal
from django.contrib.auth.models import User     # Signal sender
from django.dispatch import receiver            # Signal receiver
from .models import Profile

@receiver(post_save, sender= User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user= instance) # The instance is the User, aka the sender. This function will be fired every time someone is registered

@receiver(post_save, sender= User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
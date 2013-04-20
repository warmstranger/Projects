import apis

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    instance = kwargs['instance']
    created = kwargs['created']
    if created:
        Profile.objects.create(user=instance)
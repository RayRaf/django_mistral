from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# UserStatistics model
# ------------------------------------
# Separate models.py file to create a model that extends the User model
class UserStatistics(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    successful_image_analyses = models.IntegerField(default=0)
    successful_text_analyses = models.IntegerField(default=0)

# Signal to create or update UserStatistics whenever User is created or updated
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_or_update_user_statistics(sender, instance, created, **kwargs):
    if created:
        UserStatistics.objects.create(user=instance)
    else:
        instance.userstatistics.save()
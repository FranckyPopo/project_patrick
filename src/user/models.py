from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class PhotoProfile(models.Model):
    photo_profile = models.ImageField()
    
class Client(AbstractUser):
    choice_user = [
        ("Agent", "Agent"),
        ("Client", "Client"),
    ]
    
    photo_profile = photo_profile = models.ImageField()
    user_type = models.CharField(max_length=25, choices=choice_user)

# class Agent(AbstractUser):
#     biogaphie = models.CharField(max_length=1000)
#     facebook_link = models.URLField()
#     instagram_link = models.URLField()
#     twitter_link = models.URLField()
#     linkedin_link = models.URLField()

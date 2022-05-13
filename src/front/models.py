from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Models site
class City(models.Model):
    city = models.CharField(max_length=25)
    date_create = models.DateTimeField(default=timezone.now())
    
    def __str__(self) -> str:
        return self.city
    
class District(models.Model):
    district = models.CharField(max_length=25)
    date_create = models.DateTimeField(default=timezone.now())

    def __str__(self) -> str:
        return self.district

class SiteInfos(models.Model):
    site_title = models.CharField(max_length=25, blank=False)
    main_color = models.CharField(max_length=25, blank=False)
    full_site_color = models.CharField(max_length=25, blank=False)
    default = models.BooleanField()
    copy_rigtht = models.CharField(max_length=25)
    
class ContactSite(models.Model):
    facebook_link = models.URLField()
    instagram_link = models.URLField()
    twitter_link = models.URLField()
    linkedin_link = models.URLField()
    
    site_contact = models.IntegerField()
    email = models.EmailField()
    lang = models.CharField(max_length=25, blank=False)

class SliderSite(models.Model):
    title_image = models.CharField(max_length=25, blank=False)
    price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1_000_000)])
    photo_profile = models.ImageField()

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    
    data_create = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return self.title_image

# Model servies
class Service(models.Model):
    photo_profile = photo_profile = models.ImageField()
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=25)
    
# Model contact
class Contact(models.Model):
    nom = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.CharField(max_length=1000)
    
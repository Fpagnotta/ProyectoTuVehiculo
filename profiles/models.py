from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=20,blank=True)
    last_name = models.CharField(max_length=20,blank=True)
    phone = models.CharField(max_length=25,blank=True)
    adress = models.CharField(max_length=30,blank=True)
    city = models.CharField (max_length=30,blank=True)
    gender = models.CharField (max_length=30,blank=True)
    email = models.CharField (max_length=50,blank=True)
    image = models.ImageField(upload_to='profile_image')
    
    class Meta :
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.first_name


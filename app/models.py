from email.policy import default

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username",)
    
    



class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'articles/',blank=True)
    bio = models.TextField(blank=True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    phone_number = models.CharField(blank=True, max_length= 13)
    Id_number= models.CharField(max_length= 10)

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse('home')
 

            
    
class Station(models.Model):
    name=models.CharField(max_length= 100)
    location=models.CharField(max_length= 100)
    def __str__(self):
        return f'{self.name} station'
class Bike(models.Model):
    user_id=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bike_photo=models.ImageField(upload_to = 'articles/')
    station_Id=models.ForeignKey(Station,on_delete=models.CASCADE)
    
RATE_RIDE=[
     (1, '1 - Trash'),
     (2, '2 - Horrible'),
     (3, '3 - Terrible'),
     (4, '4 - Bad'),
     (5, '5 - Ok'),
     (6, '6 - Satisfactory'),
     (7, '7 - Good'),
     (8, '8 - Amazing'),
     (9, '9 - Perfect'),
     (10, '10 - Master Piece')
 ]
class Review(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bike=models.ForeignKey(Bike,on_delete=models.CASCADE)
    body=models.TextField()
    rate_ride=models.PositiveSmallIntegerField(choices=RATE_RIDE)
class Booking(models.Model):
    duration=models.IntegerField()
    start_time=models.DateTimeField(auto_now_add= True)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bike_id=models.ForeignKey(Bike, on_delete=models.CASCADE, default=1 )
    @property
    def total_cost(self):
        return self.duration * 200
    
    
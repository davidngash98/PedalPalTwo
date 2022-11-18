from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile,CustomUser
from django.contrib.auth.models import User
  
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
     
post_save.connect(create_profile,sender=CustomUser) 
           
def update_profile(sender,instance,created,**kwargs):
    if created == False:
        instance.profile.save()
            
post_save.connect(update_profile,sender=CustomUser)
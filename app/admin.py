from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm,CustomUserCreationForm

from app.models import Booking, Profile, Review, Station, Bike, CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email','is_staff','is_superuser']

admin.site.register(CustomUser,CustomUserAdmin)

admin.site.register(Profile)
admin.site.register(Station)
admin.site.register(Bike)
admin.site.register(Review)

class BookingAdmin(admin.ModelAdmin):
    list_display= ('id','duration','user','start_time')

admin.site.register(Booking,BookingAdmin)

# Register your models here.

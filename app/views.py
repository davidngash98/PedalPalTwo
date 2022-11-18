from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib import messages



from .forms import BookingForm, CreateProfileForm, RatingsForm, RegisterForm
from .models import Bike, Booking, Profile, Station


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    return render(request, 'Authentication/Register.html', {"form":form})
# Create your views here.
def loginPage(request):
    context ={}
    
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        user = authenticate(request,email=email,password=password)
        
        if user is not None:
            login(request,user) 
            return redirect('/')
    
    return render(request,'Authentication/login.html',context)

def index(request):
    return render(request,'index.html',{});
    
def logout_user(request):
    logout(request)
    return redirect('login')   
class CreateProfilePage(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'create_user_profile.html'
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
def profile(request, id):
    profile = Profile.objects.get(user=id)
    userid = request.user.id
    
    
    context={
        "profile":profile,
        "userid":userid,
       
    }
    return render(request, 'user_profile.html',context)
class EditProfileView(UpdateView):
    model = Profile
    template_name = 'edit.html'
    fields = ['bio','profile_photo','phone_number','Id_number']
    success_url = reverse_lazy('home')
def bike_station(request):
    stations= Station.objects.all()
    context={
        "stations":stations,
    }
    return render(request,'station.html',context)
def bike(request):
    if request.method=='POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user=request.user
            book.save()
            messages.info(request,"Booking successful!")
            return redirect('/')
    else:
        form=BookingForm()
    return render(request,'bike.html',{'form':form})
def bikesPerStation(request, station_id):
    bikez= Station.objects.get(id=station_id)
    bikes=bikez.bike_set.all()
    context={
        "bikes":bikes,
    }
    return render(request,'bikesperstation.html',context)

def bookings(request,id):
    bikez= Booking.objects.filter(user=id)
    context={
        "bikes":bikez,
    }
    return render(request,'bookings.html',context)
def rate_project(request, id):
    bike =Bike.objects.get(id=id)
    user = request.user
    
    if request.method =='POST':
        form = RatingsForm(request.POST)
        
        if form.is_valid():
            rate_ride =form.save(commit=False)
            rate_ride.user = user
            rate_ride.bike=bike
            rate_ride.save()
            return redirect('home')
        
    else:
        form = RatingsForm()
        
    return render(request, 'rate_project.html',{"bike":bike,"ratingform":form})










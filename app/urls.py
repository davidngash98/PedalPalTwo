from .views import register, loginPage, index, logout_user, CreateProfilePage, profile, EditProfileView , bike_station, bike ,bikesPerStation, rate_project, bookings
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('register/', register, name='register'),
    path('login/', loginPage, name='login'),
    re_path(r'^$', index , name='home'),
    path('logout/',logout_user,name='logout'),
    path('create_profile/', CreateProfilePage.as_view(), name='create_profile'),
    path('profile/<int:id>/', profile, name="profile"),
    path('edit/<int:pk>/',EditProfileView.as_view(), name="edit"),
    path('station/' ,bike_station, name='station'),
    path('bike/' ,bike , name='bike'),
    path('bike/<station_id>' ,bikesPerStation , name='bikes'),
    path('rate_project/<int:id>/',rate_project, name='rate_project'),
    path('booikings/<int:id>/',bookings, name='bookings'),
     ]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
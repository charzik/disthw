from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token 
from . import views

urlpatterns = [
    path('register', views.registration_view),
    path('login', obtain_auth_token),
]
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from . import views

urlpatterns = [
    path('register', views.registration_view),
    path('login', obtain_jwt_token),
    path('refresh', refresh_jwt_token),
]
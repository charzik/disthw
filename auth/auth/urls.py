from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('v1/user/', include('user.urls')),
    path('', include('proxy.urls')),
]

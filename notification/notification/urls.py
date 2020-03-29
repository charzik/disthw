from django.urls import path, include

urlpatterns = [
    path('v1/send-registartion-email', include('email_sender.urls')),
]
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('register', views.registration_view),
    path('login', views.LoginView.as_view()),
    path('refresh', TokenRefreshView.as_view()),
    path('confirm/<url_id>', views.confirm_registration_view),
]

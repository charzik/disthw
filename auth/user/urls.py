from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token

from . import views

urlpatterns = [
    path('register', views.registration_view),
    path('login', views.LoginView.as_view()),
    path('refresh', refresh_jwt_token),
    path('confirm/<url_id>', views.confirm_registration_view),
]

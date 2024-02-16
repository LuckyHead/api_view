from django.urls import path

from user.models import AbstractUser
from user.views import *

urlpatterns=[
    path('users', users),
    path('user/<int:pk>/', user_detail),
]
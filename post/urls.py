from django.urls import path

from post.views import *

urlpatterns=[
    path('', home_page),
    path('posts/', posts),
    path('posts/<int:pk>/', posts_detail),
]
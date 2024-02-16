from django.urls import path

from post_category.models import PostCategory
from post_category.views import post_categories

urlpatterns=[
    path('post_categories/', post_categories)
]
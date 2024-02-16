from django.urls import path
from post_comment.views import *

urlpatterns=[
    path('post_comments/', postcomment),
    path('detail_comment/<int:pk>/', post_comment_detail),
]
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from .settings import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('', include('user.urls')),
    path('', include('post_comment.urls')),
    path('', include('post_category.urls')),
]

# urlpatterns+=static(
#     MEDIA_URL,
#     document_root=MEDIA_ROOT
# )

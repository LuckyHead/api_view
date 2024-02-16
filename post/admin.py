from django.contrib.admin import *

from post.models import Post

@register(Post)
class PostAdmin(ModelAdmin):
    list_display=('title', 'user')
    list_display_links=('title', 'user')

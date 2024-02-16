from django.contrib.admin import *

from post_category.models import PostCategory

@register(PostCategory)
class PostCategoryAdmin(ModelAdmin):
    list_display=('name',)
    list_display_links=('name',)

from django.contrib.admin import *

from post_comment.models import PostComment

@register(PostComment)
class PostCommentAdmin(ModelAdmin):
    list_display=('user',)
    list_display_links=('user',)
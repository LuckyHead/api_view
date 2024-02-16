from django.contrib.admin import *
from .models import User

@register(User)
class UserAdmin(ModelAdmin):
    list_display=('username', 'fullname')
    list_display_links=('username', 'fullname')
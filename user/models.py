from django.db.models import *
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    fullname=CharField(
        'Fullname of user',
        max_length=16
    )
    profile_picture=ImageField(
        'Profile picture',
        upload_to='user-images/'
    )

    def __str__(self):
        return f'{self.fullname}'

    class Meta:
        verbose_name='user'
        verbose_name_plural='users'

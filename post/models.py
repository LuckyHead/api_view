from django.db.models import *

from post_category.models import PostCategory
from user.models import *

class Post(Model):
    title=CharField(
        'Title of post',
        max_length=256,
        blank=True
    )
    description=TextField(
        'Description',
        blank=True
    )
    created=DateTimeField(
        auto_now_add=True
    )
    image=FileField(
        upload_to='files/'
    )
    user=ForeignKey(
        User,
        on_delete=CASCADE,
        editable=False
    )
    watch_count=PositiveBigIntegerField(
        default=0
    )
    like_count=PositiveBigIntegerField(
        default=0
    )
    category=ForeignKey(
        PostCategory,
        on_delete=CASCADE
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
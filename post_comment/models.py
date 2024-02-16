from django.db.models import *

from post.models import Post
from user.models import User

class PostComment(Model):
    user=ForeignKey(
        User,
        on_delete=CASCADE
    )
    post=ForeignKey(
        Post,
        on_delete=CASCADE
    )
    comment=TextField(
        'Comment'
    )

    class Meta:
        verbose_name='comment'
        verbose_name_plural='comments'

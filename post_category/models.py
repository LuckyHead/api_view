from django.db.models import *

class PostCategory(Model):
    name=CharField(
        'Name of category',
        max_length=256,
        editable=False
    )
    image=ImageField(
        upload_to='category-images/',
        editable=False
    )
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name='post category'
        verbose_name_plural='post categories'
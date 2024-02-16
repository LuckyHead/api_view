from rest_framework.serializers import ModelSerializer

from post_category.models import PostCategory

class PostCategorySerializer(ModelSerializer):
    class Meta:
        model=PostCategory
        fields='__all__'
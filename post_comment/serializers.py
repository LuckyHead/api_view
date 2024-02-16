from rest_framework.serializers import ModelSerializer

from post_comment.models import PostComment

class PostCommentSerializer(ModelSerializer):
    model=PostComment
    fields='__all__'

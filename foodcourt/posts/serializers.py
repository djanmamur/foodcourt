from rest_framework.serializers import ModelSerializer, ValidationError

from ..images.serializers import ImageSerializer
from ..users.enums import UserType
from .models import Post


class PostSerializer(ModelSerializer):
    images = ImageSerializer(many=True, read_only=True,)

    class Meta:
        model = Post
        fields = ("id", "name", "description", "price", "images")


class CreatePostSerializer(ModelSerializer):
    def validate_owner(self, owner):
        if owner.user_type not in UserType.sellers():
            raise ValidationError("Only sellers can post new items")
        return owner

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    class Meta:
        model = Post
        fields = (
            "id",
            "name",
            "description",
            "price",
            "owner",
        )

from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, PostImage



User = get_user_model()

class CustomUserCreateSerializer(UserCreateSerializer):
    age = serializers.IntegerField(required=True)
    role = serializers.ChoiceField(choices=User.Role.choices, required=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'password', 'age', 'role')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ('id', 'post', 'image')

class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length = 1000000, allow_empty_file = False, use_url = False),
        write_only=True)
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'category', 'author', 'created_at', 'images', "uploaded_images")
    

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        post = Post.objects.create(**validated_data)
        for image in uploaded_images:
            newpost_image = PostImage.objects.create(post=post, image=image)
    
        return post 
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post




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
    

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['created_at']  # Exclude 'created_at' field from user input

class PostRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostDeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def validate_id(self, value):
        try:
            post = Post.objects.get(id=value)
        except Post.DoesNotExist:
            raise serializers.ValidationError("Post does not exist.")
        return value

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'text', 'category', 'author', 'image']

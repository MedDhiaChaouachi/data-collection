from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class CustomUserCreateSerializer(UserCreateSerializer):
    age = serializers.IntegerField(required=True)
    role = serializers.ChoiceField(choices=User.Role.choices, required=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'age', 'role')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *

# User Serializer
class UserGetSerializer(serializers.ModelSerializer):
    friend_requests = serializers.SerializerMethodField(required=False, read_only=True)
    friends = serializers.SerializerMethodField(required=False, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'friend_requests', 'friends')

    def get_friend_requests(self, user):
        count = 0
        request_list = []
        for requests in user.to_user.all():
            count += 1
            request = {
                "id": requests.from_user.id,
                "name": f'{requests.from_user.first_name} {requests.from_user.last_name}'
                }
            request_list.append(request)
        return {
            "request_number": count,
            "requests": request_list
        }

    def get_friends(self, user):
        friend_list = []
        for friend in User.objects.filter(friends_set__users__id=user.id).exclude(id=user.id):
            friend_list.append({
                "id": friend.id
            })
        return friend_list


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

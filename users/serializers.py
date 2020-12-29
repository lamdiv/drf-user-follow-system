from djoser.serializers import UserCreateSerializer,UserSerializer
from rest_framework import serializers
from .models import User,UserContact

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','name','username','email','password')


class UserContactSerializer(serializers.ModelSerializer):
    action = serializers.CharField()
    class Meta:
        model = UserContact
        fields = ('user_to','action')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','username')


class UserFollowingSerializer(serializers.ModelSerializer):
    following = UserSerializer(many=True,read_only=True)
    followers = UserSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = ('following','followers')

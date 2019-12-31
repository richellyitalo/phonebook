from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Contact


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class ContactSerializer(serializers.ModelSerializer):
    # user = UserSerializer(default=serializers.CurrentUserDefault())

    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True, source='user', default=serializers.CurrentUserDefault())

    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ('user',)

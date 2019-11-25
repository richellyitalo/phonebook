from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Contact


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class ContactSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ('user',)

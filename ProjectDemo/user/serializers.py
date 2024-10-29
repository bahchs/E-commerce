from rest_framework import serializers
from .models import CustomerUser


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerUser
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username= serializers.CharField()
    password= serializers.CharField()
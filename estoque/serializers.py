from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
    def create(self, clean_data):
        user_obj = CustomUser.objects.create_user(email = clean_data['email'],
            password=clean_data['password'])
        user_obj.first_name = clean_data['first_name']
        user_obj.save()
        return user_obj

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    ##
    def check_user(self, clean_data):
        user = authenticate(email=clean_data['email'], password=clean_data[
            'password'])
        if not user:
            raise ValidationError('User not found')
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name')
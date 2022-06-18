from rest_framework import serializers
from .models import CustomUser, Firm
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from config.settings import AUTH_USER_MODEL

User = AUTH_USER_MODEL


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password2', 'email',  'image', 'auth', 'firm', 'phone_number')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            image=validated_data['image'],
            auth=validated_data['auth'],
            firm=validated_data['firm'],
            phone_number=validated_data['phone_number']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'image', 'auth', 'firm', 'phone_number',]


class FirmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ['name', 'image', 'viloyat', 'tuman', 'about']

from rest_framework import serializers
from rest_framework.validators import ValidationError
from ..models import Employee


class EmployeeCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=150)
    password = serializers.CharField(min_length=8, max_length=128)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)

    class Meta:
        model = Employee
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def validate(self, attrs):
        email_exists=Employee.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise ValidationError('Email already exists')

        username_exists=Employee.objects.filter(username=attrs['username']).exists()
        if username_exists:
            raise ValidationError('Username already exists')

        return super().validate(attrs)

    def create(self, validated_data):
        user = Employee.objects.create_user(**validated_data)

        return user
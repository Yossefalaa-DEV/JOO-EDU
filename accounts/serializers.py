from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student

class UserSerializer(serializers.ModelSerializer):
    """
    محول بيانات المستخدم
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class StudentSerializer(serializers.ModelSerializer):
    """
    محول بيانات الطالب
    """
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ('id', 'user', 'phone_number', 'created_at')

class RegisterSerializer(serializers.Serializer):
    """
    محول بيانات التسجيل
    """
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        # إنشاء مستخدم جديد
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        
        # إنشاء طالب جديد
        student = Student.objects.create(
            user=user,
            phone_number=validated_data['phone_number']
        )
        
        return student

class LoginSerializer(serializers.Serializer):
    """
    محول بيانات تسجيل الدخول
    """
    username = serializers.CharField()
    password = serializers.CharField(write_only=True) 
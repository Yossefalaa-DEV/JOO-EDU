from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from .serializers import (
    UserSerializer, StudentSerializer, RegisterSerializer, LoginSerializer
)
from .models import Student, ActivationCode
from videos.models import Video
import random
import string
from rest_framework.authtoken.serializers import AuthTokenSerializer

class RegisterAPI(generics.GenericAPIView):
    """
    واجهة تسجيل مستخدم جديد
    """
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class GenerateActivationCodeAPI(generics.GenericAPIView):
    """
    واجهة توليد أكواد تفعيل
    """
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        prefix = request.data.get('prefix', '')
        video_id = request.data.get('video_id')
        max_views = request.data.get('max_views', 1)

        if not video_id:
            return Response(
                {"error": "Video ID is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Generate random suffix
        suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        code = f"{prefix}{suffix}"

        # Create activation code
        activation_code = ActivationCode.objects.create(
            code=code,
            video_id=video_id,
            max_views=max_views
        )

        return Response({
            "code": activation_code.code,
            "video_id": activation_code.video_id,
            "max_views": activation_code.max_views,
            "created_at": activation_code.created_at
        })

class ValidateActivationCodeAPI(generics.GenericAPIView):
    """
    واجهة التحقق من كود التفعيل
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        code = request.data.get('code')
        if not code:
            return Response(
                {"error": "Activation code is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            activation_code = ActivationCode.objects.get(code=code)
            if activation_code.is_valid():
                activation_code.views_count += 1
                activation_code.save()
                return Response({
                    "valid": True,
                    "video_id": activation_code.video_id,
                    "remaining_views": activation_code.max_views - activation_code.views_count
                })
            else:
                return Response({
                    "valid": False,
                    "error": "Code has reached maximum views"
                })
        except ActivationCode.DoesNotExist:
            return Response({
                "valid": False,
                "error": "Invalid activation code"
            }) 
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Course, Video
from .serializers import CourseSerializer, VideoSerializer
from accounts.models import ActivationCode

class CourseListAPI(generics.ListCreateAPIView):
    """
    واجهة عرض وإنشاء الدورات
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Course.objects.all()
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category=category)
        return queryset

class CourseDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    واجهة عرض وتحديث وحذف دورة محددة
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

class VideoListAPI(generics.ListCreateAPIView):
    """
    واجهة عرض وإنشاء الفيديوهات
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Video.objects.all()
        course_id = self.request.query_params.get('course', None)
        if course_id:
            queryset = queryset.filter(course_id=course_id)
        return queryset

class VideoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    واجهة عرض وتحديث وحذف فيديو محدد
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # التحقق من وجود كود تفعيل صالح
        activation_code = request.query_params.get('code', None)
        if not activation_code:
            return Response(
                {"error": "Activation code is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            code = ActivationCode.objects.get(code=activation_code, video=instance)
            if not code.is_valid():
                return Response(
                    {"error": "Invalid or expired activation code"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except ActivationCode.DoesNotExist:
            return Response(
                {"error": "Invalid activation code"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(instance)
        return Response(serializer.data) 
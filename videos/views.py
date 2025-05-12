from rest_framework import generics, permissions
from .models import Video
from .serializers import VideoSerializer

class VideoListAPI(generics.ListAPIView):
    """
    واجهة عرض قائمة الفيديوهات
    """
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        return Video.objects.filter(course_id=course_id, is_active=True)

class VideoDetailAPI(generics.RetrieveAPIView):
    """
    واجهة عرض تفاصيل الفيديو
    """
    queryset = Video.objects.filter(is_active=True)
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated] 
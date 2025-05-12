from rest_framework import serializers
from .models import Video
from courses.serializers import CourseSerializer

class VideoSerializer(serializers.ModelSerializer):
    """
    محول بيانات الفيديو التعليمي
    """
    course = CourseSerializer(read_only=True)
    course_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Video
        fields = ('id', 'title', 'description', 'youtube_url', 'course', 'course_id', 
                 'order', 'is_active', 'created_at') 
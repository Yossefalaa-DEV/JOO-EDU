from django.db import models
from courses.models import Course

class Video(models.Model):
    """
    نموذج الفيديو التعليمي
    يحتوي على معلومات الفيديو وروابط يوتيوب
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    youtube_url = models.URLField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.course.title}"

    class Meta:
        ordering = ['course', 'order'] 
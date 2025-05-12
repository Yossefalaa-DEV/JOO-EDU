from django.db import models
from django.contrib.auth.models import User
from courses.models import Course
from videos.models import Video

class Student(models.Model):
    """
    نموذج الطالب
    يحتوي على معلومات الطالب الأساسية
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.phone_number}"

class ActivationCode(models.Model):
    """
    نموذج كود التفعيل
    يستخدم لتفعيل فيديو محدد
    """
    prefix = models.CharField(max_length=3, default='ABC')  # قيمة افتراضية للبادئة
    code = models.CharField(max_length=7, unique=True)  # الكود الكامل (7 أحرف)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    uses_left = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.code} - {self.video.title} - {self.uses_left} uses left"

    class Meta:
        ordering = ['-created_at'] 
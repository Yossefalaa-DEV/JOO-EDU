from django.contrib import admin
from .models import Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'course')
    search_fields = ('title', 'description')
    list_select_related = ('course',) 
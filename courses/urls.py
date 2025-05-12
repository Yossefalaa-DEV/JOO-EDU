from django.urls import path
from .views import (
    CourseListAPI,
    CourseDetailAPI,
    VideoListAPI,
    VideoDetailAPI,
)

urlpatterns = [
    path('', CourseListAPI.as_view(), name='course-list'),
    path('<int:pk>/', CourseDetailAPI.as_view(), name='course-detail'),
    path('videos/', VideoListAPI.as_view(), name='video-list'),
    path('videos/<int:pk>/', VideoDetailAPI.as_view(), name='video-detail'),
] 
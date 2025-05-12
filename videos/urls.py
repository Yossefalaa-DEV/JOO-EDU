from django.urls import path
from .views import VideoListAPI, VideoDetailAPI
 
urlpatterns = [
    path('course/<int:course_id>/', VideoListAPI.as_view(), name='video-list'),
    path('<int:pk>/', VideoDetailAPI.as_view(), name='video-detail'),
] 
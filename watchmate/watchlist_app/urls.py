from django.urls import path
from .views import StreamingPlatformAV, WatchListAV, WatchDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='details'),
    path('streamer', StreamingPlatformAV.as_view(), name='streaming_platform_list'),
]
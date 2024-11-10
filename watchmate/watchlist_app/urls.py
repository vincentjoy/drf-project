from django.urls import path
from .views import WatchListAV, WatchDetailAV, StreamingPlatformAV, StreamingPlatformDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='details'),
    path('streamer', StreamingPlatformAV.as_view(), name='streaming_platform_list'),
    path('streamer/<int:pk>', StreamingPlatformDetailAV.as_view(), name='streaming_platform_details'),
]
from django.urls import path
from .views import WatchListAV, WatchDetailAV, StreamingPlatformAV, StreamingPlatformDetailAV, ReviewList, ReviewDetail

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='details'),
    path('streamer', StreamingPlatformAV.as_view(), name='streaming_platform_list'),
    path('streamer/<int:pk>', StreamingPlatformDetailAV.as_view(), name='streaming_platform_details'),
    path('review', ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review_detail'),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (WatchListAV, WatchDetailAV,
                    StreamingPlatformVS,
                    ReviewList, ReviewDetail, ReviewCreate)

router = DefaultRouter()
router.register('streamer', StreamingPlatformVS, basename='streaming_platform'),

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='details'),
    path('', include(router.urls)),
    path('streamer/<int:pk>/review-create', ReviewCreate.as_view(), name='review_create'),
    path('streamer/<int:pk>/review', ReviewList.as_view(), name='review_list'),
    path('streamer/review/<int:pk>', ReviewDetail.as_view(), name='review_detail'),
]
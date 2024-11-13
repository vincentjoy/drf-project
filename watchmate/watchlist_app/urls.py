from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (WatchListAV, WatchDetailAV, WatchListSearch, WatchListSort,
                    StreamingPlatformVS,
                    ReviewList, ReviewDetail, ReviewCreate,
                    UserReview)

router = DefaultRouter()
router.register('streamer', StreamingPlatformVS, basename='streaming_platform'),

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('listsearch/', WatchListSearch.as_view(), name='watch_list_search'),
    path('listsort/', WatchListSort.as_view(), name='watch_list_sort'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='details'),
    path('', include(router.urls)),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review_create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),
    path('reviews/', UserReview.as_view(), name='user_review_detail'),
]
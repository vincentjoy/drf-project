from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('streamer', views.StreamingPlatformVS, basename='streaming_platform'),

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='watch_list'),
    path('listsearch/', views.WatchListSearch.as_view(), name='watch_list_search'),
    path('listsort/', views.WatchListSort.as_view(), name='watch_list_sort'),
    path('<int:pk>/', views.WatchDetailAV.as_view(), name='details'),
    path('', include(router.urls)),
    path('<int:pk>/reviews/create/', views.ReviewCreate.as_view(), name='review_create'),
    path('<int:pk>/reviews/', views.ReviewList.as_view(), name='review_list'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('user/reviews/', views.UserReview.as_view(), name='user_review_detail'),
]
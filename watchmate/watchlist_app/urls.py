from django.urls import path
# from .views import movie_list, movie_details
from .views import MovieList, MovieDetail

urlpatterns = [
    path('list/', MovieList.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie_details'),
]
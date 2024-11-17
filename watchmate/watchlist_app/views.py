from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import ScopedRateThrottle, AnonRateThrottle
from rest_framework import status, generics, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from . import models, serializers
from watchlist_app.api import permissions, throttling
from watchlist_app.api.pagination import WatchListPagination


class UserReview(generics.ListAPIView):
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        return models.Review.objects.filter(review_user__username=username)


class ReviewCreate(generics.CreateAPIView):
    serializer_class = serializers.ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [throttling.ReviewCreateThrottle]

    def get_queryset(self):
        return models.Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = models.WatchList.objects.get(pk=pk)

        user = self.request.user
        review_queryset = models.Review.objects.filter(review_user=user, watchlist=watchlist)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie.")

        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating * watchlist.number_rating + serializer.validated_data['rating']) / (watchlist.number_rating + 1)
        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()

        serializer.save(watchlist=watchlist, review_user=user)


class ReviewList(generics.ListAPIView):
    serializer_class = serializers.ReviewSerializer
    throttle_classes = [throttling.ReviewListThrottel, AnonRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review_user__username']

    def get_queryset(self):
        pk = self.kwargs['pk']
        return models.Review.objects.filter(watchlist=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminOrReadOnly]
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.IsReviewUserOrReadOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'review_detail'


class StreamingPlatformVS(viewsets.ModelViewSet):
    queryset = models.StreamingPlatform.objects.all()
    serializer_class = serializers.StreamingPlatformSerializer


class WatchListSearch(generics.ListAPIView):
    queryset = models.WatchList.objects.all()
    serializer_class = serializers.WatchListSerializer
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['title', 'platform__name']


class WatchListSort(generics.ListAPIView):
    queryset = models.WatchList.objects.all()
    serializer_class = serializers.WatchListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_filters = ['avg_rating']
    pagination_class = WatchListPagination


class WatchListAV(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]

    def get(self, request):
        movies = models.WatchList.objects.all()
        serializer = serializers.WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchDetailAV(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]

    def get(self, request, pk):
        try:
            movie = models.WatchList.objects.get(pk=pk)
        except models.WatchList.DoesNotExist:
            return Response({'Error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = models.WatchList.objects.get(pk=pk)
        serializer = serializers.WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = models.WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
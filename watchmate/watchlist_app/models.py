from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class StreamingPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=150)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    synopsis = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamingPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    avg_rating = models.FloatField(default=0)
    number_rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.CharField(max_length=500, null=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.rating}/5 rating for {self.watchlist.title}"

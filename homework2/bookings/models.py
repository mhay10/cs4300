from django.contrib.auth.models import User
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="seats")
    seat_number = models.CharField(max_length=10)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.movie.title} - {self.seat_number}"

    class Meta:
        unique_together = ["movie", "seat_number"]
        ordering = ["seat_number"]

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - {self.seat.seat_number}"

    class Meta:
        ordering = ["-booking_date"]

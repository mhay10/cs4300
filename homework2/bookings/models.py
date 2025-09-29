from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.TextField()
    desc = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Seat(models.Model):
    seat_num = models.TextField(unique=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.seat_num


class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="bookings")
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name="bookings")
    user = models.TextField()
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -> {self.movie.title} -> {self.seat.seat_num}"
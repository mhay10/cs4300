from rest_framework import serializers
from .models import Movie, Seat, Booking


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    seat = SeatSerializer(read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(), write_only=True, source="movie"
    )
    seat_id = serializers.PrimaryKeyRelatedField(
        queryset=Seat.objects.all(), write_only=True, source="seat"
    )

    class Meta:
        model = Booking
        fields = [
            "id",
            "movie",
            "seat",
            "user",
            "booking_date",
            "movie_id",
            "seat_id",
        ]

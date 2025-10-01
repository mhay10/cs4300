from rest_framework import serializers
from .models import Movie, Seat, Booking

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "release_date", "duration"]

class SeatSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)

    class Meta:
        model = Seat
        fields = ["id", "movie" "movie_title", "seat_number", "status"]

class BookingSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    seat_number = serializers.CharField(source="seat.seat_number", read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Booking
        fields = ["id", "movie", "movie_title", "seat", "seat_number", "username", "booking_date"]
        read_only_fields = ["booking_date"]

    # Check if seat is available before creating a booking
    def create(self, validated_data):
        seat = validated_data["seat"]
        if not seat.status:
            raise serializers.ValidationError("Seat is not available")

        booking = Booking.objects.create(**validated_data)
        seat.status = False
        seat.save()

        return booking
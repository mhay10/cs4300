from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer


# API Views
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    # Get all available seats
    @action(detail=False, methods=["get"])
    def available(self, request):
        movie_id = request.query_params.get("movie_id")
        if movie_id:
            seats = Seat.objects.filter(movie_id=movie_id, status=True)
        else:
            seats = Seat.objects.filter(status=True)

        serializer = SeatSerializer(seats, many=True)
        return Response(serializer.data)


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    # Filter bookings by user
    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get("user_id")
        if user_id:
            queryset = queryset.filter(user_id=user_id)

        return queryset


# HTML Views
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "bookings/movie_list.html", {"movies": movies})


def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(movie=movie)

    # Create new booking if POST request
    if request.method == "POST":
        seat_id = request.POST.get("seat_id")
        seat = get_object_or_404(Seat, id=seat_id)

        if seat.status:
            user, created = User.objects.get_or_create(username="demo")

            Booking.objects.create(movie=movie, seat=seat, user=user)
            seat.status = False
            seat.save()

            return redirect("booking_history")

    return render(
        request, "bookings/seat_booking.html", {"movie": movie, "seats": seats}
    )


def booking_history(request):
    bookings = Booking.objects.all()
    return render(request, "bookings/booking_history.html", {"bookings": bookings})

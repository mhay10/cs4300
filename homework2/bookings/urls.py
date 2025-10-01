from django.urls import path
from . import views

urlpatterns = [
    path("", views.movie_list, name="movie_list"),
    path("movie/<int:movie_id>/seats/", views.seat_booking, name="book_seat"),
    path("bookings/", views.booking_history, name="booking_history"),
]
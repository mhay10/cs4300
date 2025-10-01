from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from datetime import date


class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test",
            description="Test movie",
            release_date=date(2025, 1, 1),
            duration=120,
        )

    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "Test")
        self.assertEqual(self.movie.description, "Test movie")
        self.assertEqual(self.movie.release_date, date(2025, 1, 1))
        self.assertEqual(self.movie.duration, 120)

    def test_movie_str(self):
        self.assertEqual(str(self.movie), "Test")


class SeatModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test",
            description="Test movie",
            release_date=date(2025, 1, 1),
            duration=120,
        )
        self.seat = Seat.objects.create(
            movie=self.movie,
            seat_number="A1",
            status=True,
        )

    def test_seat_creation(self):
        self.assertEqual(self.seat.movie, self.movie)
        self.assertEqual(self.seat.seat_number, "A1")
        self.assertEqual(self.seat.status, True)

    def test_seat_str(self):
        self.assertEqual(str(self.seat), "Test - A1")


class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.movie = Movie.objects.create(
            title="Test",
            description="Test movie",
            release_date=date(2025, 1, 1),
            duration=120,
        )
        self.seat = Seat.objects.create(
            movie=self.movie,
            seat_number="A1",
            status=True,
        )
        self.booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user,
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.movie, self.movie)
        self.assertEqual(self.booking.seat, self.seat)
        self.assertEqual(self.booking.user, self.user)

class APITest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test",
            description="Test movie",
            release_date=date(2025, 1, 1),
            duration=120,
        )

    def test_movie_list_api(self):
        response = self.client.get("/api/movies/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_movie_detail_api(self):
        response = self.client.get(f"/api/movies/{self.movie.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["title"], "Test")
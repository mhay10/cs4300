from django.test import TestCase
from .models import Movie
from datetime import date

class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test",
            description="Test movie",
            release_date=date(2025, 1, 1),
            duration=120
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
            duration=120
        )
        self.seat = self.movie.seats.create(
            movie=self.movie,
            seat_number="A1",
            status=True
        )

    def test_seat_creation(self):
        self.assertEqual(self.seat.movie, self.movie)
        self.assertEqual(self.seat.seat_number, "A1")
        self.assertEqual(self.seat.status, True)

    def test_seat_str(self):
        self.assertEqual(str(self.seat), "A1")


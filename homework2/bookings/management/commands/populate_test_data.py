from django.core.management.base import BaseCommand
from bookings.models import Movie, Seat
from datetime import date

class Command(BaseCommand):
    help = "Populates database with test data"

    def handle(self, *args, **kwargs):
        test_movies = [
            {
                'title': 'The Matrix',
                'description': 'A computer hacker learns about the true nature of reality.',
                'release_date': date(1999, 3, 31),
                'duration': 136
            },
            {
                'title': 'Inception',
                'description': 'A thief who steals secrets through dream-sharing technology.',
                'release_date': date(2010, 7, 16),
                'duration': 148
            },
            {
                'title': 'Interstellar',
                'description': 'A team of explorers travel through a wormhole in space.',
                'release_date': date(2014, 11, 7),
                'duration': 169
            }
        ]

        for movie_data in test_movies:
            movie, created = Movie.objects.get_or_create(**movie_data)
            if created:
                # Create 10 seats for each movie
                for row in ("A", "B", "C", "D"):
                    for num in range(1, 11):
                        seat = Seat.objects.create(
                            movie=movie,
                            seat_number=f"{row}{num}",
                            status=True,
                        )

                print(f"Created movie: {movie.title} with {movie.seats.count()} seats")

        print("Done!")
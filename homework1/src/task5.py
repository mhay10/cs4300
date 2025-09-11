def get_favorite_books():
    """Returns of my favorite books series with their titles and authors"""

    # List of books in the format: (title, author)
    books = [
        ("The 3 Body Problem", "Liu Cixin"),
        ("Children of Time", "Adrian Tchaikovsky"),
        ("Mistborn", "Brandon Sanderson"),
        ("Arc of a Scythe", "Neal Shusterman"),
        ("Harry Potter", "J.K. Rowling"),
        ("Kingdom Keepers", "Ridley Pearson"),
    ]
    return books


def get_first_3_books(books: list[tuple[str, str]]):
    """Get first 3 books from list of books argument"""

    return books[:3]


def get_student_db():
    """Returns a dictionary of student names and ids"""

    # Dict of students in format: {name: id}
    students = {
        "Max": "S001",
        "Jayden": "S002",
        "Vincent": "S003",
        "Tyler": "S004",
        "Kim": "S005",
        "Sara": "S006",
        "Amerie": "S007",
        "Natalija": "S008",
    }
    return students

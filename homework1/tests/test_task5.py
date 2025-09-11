from src import task5
import pytest

# Test list of favorite books is list and format is correct
def test_book_list():
    # Make sure list of books is list
    books = task5.get_favorite_books()
    assert isinstance(books, list)

    # Make sure each book is format: (title, author)
    for book in books:
        assert isinstance(book, tuple)
        assert len(book) == 2

# Test slice of first 3 books match
def test_book_slice():
    # Get first 3 from favorite books
    books = task5.get_favorite_books()
    first3 = task5.get_first_3_books(books)

    # Make sure length is 3 and matches original list
    assert len(first3) == 3
    assert first3 == books[:3]

# Test student db structure
def test_student_db():
    students = task5.get_student_db()

    # Make sure students db is dict and length match
    assert isinstance(students, dict)
    assert len(students) == 8

    # Make sure all student ids start with 'S'
    for sid in students.values():
        assert type(sid) == str
        assert sid.startswith("S")

if __name__ == "__main__":
    test_book_list()
    test_book_slice()
    test_student_db()


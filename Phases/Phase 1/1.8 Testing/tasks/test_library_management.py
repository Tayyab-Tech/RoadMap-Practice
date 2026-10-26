# Design a complete test suite for a mini Library Management System covering book borrowing, returning, searching, and user validation.
import pytest
from library_managment import Library

def test_add_book():
    library = Library()
    library.add_book("Python Basics")
    assert library.search_book("Python Basics") is not None

def test_search_book():
    library = Library()
    library.add_book("Python Basics")
    result = library.search_book("Python Basics")
    assert result["title"] == "Python Basics"

def test_book_not_found():
    library = Library()
    assert library.search_book("Java") is None

def test_register_user():
    library = Library()
    library.register_user("user1")
    assert "user1" in library.users

def test_invalid_user():
    library = Library()
    library.add_book("Python Basics")
    with pytest.raises(ValueError):
        library.borrow_book("unknown", "Python Basics")

def test_borrow_book():
    library = Library()
    library.add_book("Python Basics")
    library.register_user("user1")
    library.borrow_book("user1", "Python Basics")
    book = library.search_book("Python Basics")
    assert book["borrowed"] is True
    assert "Python Basics" in library.users["user1"]


def test_borrow_already_borrowed_book():
    library = Library()
    library.add_book("Python Basics")
    library.register_user("user1")
    library.register_user("user2")
    library.borrow_book("user1", "Python Basics")
    with pytest.raises(ValueError):
        library.borrow_book("user2", "Python Basics")

def test_return_book():
    library = Library()
    library.add_book("Python Basics")
    library.register_user("user1")
    library.borrow_book("user1", "Python Basics")
    library.return_book("user1", "Python Basics")
    book = library.search_book("Python Basics")
    assert book["borrowed"] is False
    assert "Python Basics" not in library.users["user1"]
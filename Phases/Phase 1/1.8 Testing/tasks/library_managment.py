# Design a complete test suite for a mini Library Management System covering book borrowing, returning, searching, and user validation.
class Library:

    def __init__(self):
        self.books = []
        self.users = {}

    def add_book(self, book):
        self.books.append({
            "title": book,
            "borrowed": False
        })

    def register_user(self, user_id):
        self.users[user_id] = []

    def search_book(self, title):
        for book in self.books:
            if book["title"] == title:
                return book

        return None

    def borrow_book(self, user_id, title):

        if user_id not in self.users:
            raise ValueError("Invalid user")

        book = self.search_book(title)

        if book is None:
            raise ValueError("Book not found")

        if book["borrowed"]:
            raise ValueError("Book already borrowed")

        book["borrowed"] = True
        self.users[user_id].append(title)

    def return_book(self, user_id, title):

        if user_id not in self.users:
            raise ValueError("Invalid user")

        if title not in self.users[user_id]:
            raise ValueError("Book was not borrowed")

        book = self.search_book(title)
        book["borrowed"] = False

        self.users[user_id].remove(title)

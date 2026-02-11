# 1. Create a class TextLogger that appends new messages into a log file.

# class TextLogger:

#     def __init__(self, filename = "log.txt"):
#         self.filename = filename

#     def log(self, messages):
#         self.messages = messages
#         with open(self.filename,  "a") as file:
#             file.write(messages + "\n")


class JSONLibrary:
    def __init__(self, filename="library.json"):
        self.filename = filename

    def load_books(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self, books):
        with open(self.filename, "w") as file:
            json.dump(books, file, indent=4)

    def add_book(self, title, author):
        books = self.load_books()
        books.append({"title": title, "author": author})
        self.save_books(books)

    def list_books(self):
        return self.load_books()

    def delete_book(self, title):
        books = self.load_books()
        books = [book for book in books if book["title"] != title]
        self.save_books(books)

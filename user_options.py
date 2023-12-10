from menu import Menu
from filehandler import FileHandler as Fh


class UserInterface:

    def run(self):
        while True:
            Menu.show_user_menu()
            user_instruction = input("Wybierz opcję: ")

            if user_instruction == "1":
                self.borrow_book()
            elif user_instruction == "2":
                self.reserve_book()
            elif user_instruction == "3":
                self.extend_loan()
            elif user_instruction == "4":
                self.show_all_books()
            elif user_instruction == "4.1":
                title = input("Wprowadź tytuł, którego szukasz: ")
                self.search_by_title(title)
            elif user_instruction == "4.2":
                author = input("Wprowadź autora, którego szukasz: ")
                self.search_by_author(author)
            elif user_instruction == "4.3":
                keywords_input = input("Wprowadź słowa kluczowe oddzielone spacjami: ")
                book_keywords = keywords_input.split()
                self.search_by_keywords(book_keywords)
            else:
                print("Nieprawidłowe polecenie. Spróbuj ponownie.")

    def borrow_book(self):
        pass

    def reserve_book(self):
        pass

    def extend_loan(self):
        pass

    @staticmethod
    def display_found_books(found_books):
        if not found_books:
            print("Brak pasujących książek.")
        else:
            print("Znalezione książki:")

            for found_book in found_books:
                print("\n---")
                print(f"Tytuł: {found_book['Title']}")
                print(f"Autor: {found_book['Author']}")
                print(f"Status wypożyczenia: {'Wypożyczona' if found_book['IsBorrowed'] else 'Dostępna'}")

    def show_all_books(self):
        self.display_found_books(Fh.load_books_data()["books"])

    def search_by_title(self, title):
        found_books = [book for book in Fh.load_books_data()["books"] if book["Title"] == title]
        self.display_found_books(found_books)

    def search_by_author(self, author):
        found_books = [book for book in Fh.load_books_data()["books"] if book["Author"] == author]
        self.display_found_books(found_books)

    def search_by_keywords(self, book_keywords):
        found_books = [book for book in Fh.load_books_data()["books"] if
                       all(keyword in book["Keywords"] for keyword in book_keywords)]
        self.display_found_books(found_books)

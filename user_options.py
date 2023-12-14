from datetime import datetime, timedelta

from filehandler import FileHandler as Fh
from menu import Menu


class UserInterface:
    current_user_login = None

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

    def borrow_book(self) -> None:
        book_title = input("Wprowadź tytuł książki do wypożyczenia: ")
        books = Fh.load_books_data()["books"]

        for book in books:
            if book["title"].lower() == book_title.lower():
                if book["borrow_status"]:
                    print(f"Książka '{book_title}' jest już wypożyczona.")
                    return
                else:
                    book["borrow_status"] = True
                    book["borrow_date"] = datetime.now().strftime("%Y-%m-%d")
                    book["return_date"] = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
                    book["borrowed_by"] = self.current_user_login
                    Fh.save_books_data({"books": books})
                    print(f"Książka '{book_title}' została wypożyczona.")
                    return

        print(f"Książka o tytule '{book_title}' nie została znaleziona.")

    def reserve_book(self) -> None:
        book_title = input("Wprowadź tytuł książki do zarezerwowania: ")
        books = Fh.load_books_data()["books"]

        for book in books:
            if book["title"].lower() == book_title.lower():
                if book["borrow_status"]:
                    if self.current_user_login not in book.get("reserved_by", []):
                        book.setdefault("reserved_by", []).append(self.current_user_login)
                        Fh.save_books_data({"books": books})
                        print(f"Książka '{book_title}' została zarezerwowana.")
                    else:
                        print("Już zarezerwowałeś tę książkę.")
                else:
                    print("Książka jest dostępna do wypożyczenia.")
                return

        print(f"Książka o tytule '{book_title}' nie została znaleziona.")

    def extend_loan(self) -> None:
        books = Fh.load_books_data()["books"]
        borrowed_books = [book for book in books if
                          book["borrowed_by"] == self.current_user_login and book["borrow_status"]]

        if not borrowed_books:
            print("Nie masz żadnych wypożyczonych książek.")
            return

        if len(borrowed_books) > 1:
            print("Masz wypożyczone następujące książki:")
            for i, book in enumerate(borrowed_books, 1):
                print(f"{i}. {book['title']} - data zwrotu: {book['return_date']}")
            book_index = int(input("Wybierz numer książki, którą chcesz przedłużyć: ")) - 1
            selected_book = borrowed_books[book_index]
        else:
            selected_book = borrowed_books[0]

        new_return_date = datetime.strptime(selected_book["return_date"], "%Y-%m-%d") + timedelta(days=7)
        selected_book["return_date"] = new_return_date.strftime("%Y-%m-%d")
        Fh.save_books_data({"books": books})
        print(f"Przedłużono wypożyczenie książki '{selected_book['title']}' do {selected_book['return_date']}.")

    @staticmethod
    def display_found_books(found_books) -> None:
        if not found_books:
            print("Brak pasujących książek.")
        else:
            print("Znalezione książki:")

            for found_book in found_books:
                print("\n---")
                print(f"Tytuł: {found_book['title']}")
                print(f"Autor: {found_book['author']}")
                print(f"Status wypożyczenia: {'Wypożyczona' if found_book['borrow_status'] else 'Dostępna'}")

    def show_all_books(self) -> None:
        self.display_found_books(Fh.load_books_data()["books"])

    def search_by_title(self, title) -> None:
        found_books = [book for book in Fh.load_books_data()["books"] if book["title"].lower() == title.lower()]
        self.display_found_books(found_books)

    def search_by_author(self, author) -> None:
        found_books = [book for book in Fh.load_books_data()["books"] if book["author"].lower() == author.lower()]
        self.display_found_books(found_books)

    def search_by_keywords(self, book_keywords) -> None:
        found_books = [book for book in Fh.load_books_data()["books"] if
                       all(keyword.lower() in (kw.lower() for kw in book["keywords"]) for keyword in book_keywords)]
        self.display_found_books(found_books)

from filehandler import FileHandler as Fh
from menu import Menu
from security.cipher import Cipher
from user_options import UserInterface as Ui


class EmployeeInterface:
    current_employee_login = None

    def run(self):
        while True:
            Menu.show_employee_menu()
            user_instruction = input("Wybierz opcję: ")

            if user_instruction == "1":
                self.accept_return()
            elif user_instruction == "2":
                self.add_new_book()
            elif user_instruction == "3":
                self.remove_book()
            elif user_instruction == "4":
                self.add_reader()
            elif user_instruction == "5":
                self.browse_catalog()
            elif user_instruction == "6":
                self.logout()
                break
            else:
                print("Nieprawidłowe polecenie. Spróbuj ponownie.")

    def accept_return(self):
        # Implementacja funkcji przyjmowania zwrotu książki
        pass

    def add_new_book(self):
        title = input("Podaj tytuł książki: ")
        author = input("Podaj autora książki: ")
        keywords = input("Podaj słowa kluczowe (oddzielone przecinkiem): ").split(',')

        new_book = {
            "title": title,
            "author": author,
            "borrow_status": False,
            "borrow_date": None,
            "return_date": None,
            "borrowed_by": None,
            "reserved_by": None,
            "keywords": keywords
        }

        books_data = Fh.load_books_data()["books"]
        books_data.append(new_book)
        Fh.save_books_data(books_data)
        print(f"Dodano książkę '{title}' do katalogu.")

    def remove_book(self):
        title_to_remove = input("Podaj tytuł książki do usunięcia: ")

        books_data = Fh.load_books_data()["books"]
        books_data = [book for book in books_data if book['title'] != title_to_remove]

        Fh.save_books_data({"books": books_data})
        print(f"Usunięto książkę '{title_to_remove}' z katalogu.")

    def add_reader(self):
        print("\nRejestracja nowego czytelnika:")
        while True:
            login = input("Podaj login (lub wpisz 'end' aby wrócić do menu głównego): ")

            if login.lower() == 'end':
                return  # Wróć do menu głównego
            elif Fh.check_login_availability(login, Fh.USER_DATA):
                break
            else:
                print("Podany login już istnieje. Proszę podać inny login.")

        password = input("Podaj hasło: ")
        cipher = Cipher()
        hashed_password = cipher.hash_data(password)
        Fh.save_credentials(login, hashed_password, Fh.USER_DATA)
        print(f"Utworzono konto czytelnika '{login}'.")

    def browse_catalog(self):
        Ui.display_found_books(Fh.load_books_data()["books"])

    @staticmethod
    def logout():
        print("Wylogowano pracownika.")

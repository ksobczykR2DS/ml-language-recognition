from menu import Menu


class UserInterface:
    def __init__(self, library_system):
        self.library_system = library_system

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
                self.search_by_title()
            elif user_instruction == "4.2":
                self.search_by_author()
            elif user_instruction == "4.3":
                self.search_by_keywords()

            elif user_instruction == "5":
                self.logout()
                break
            else:
                print("Nieprawidłowe polecenie. Spróbuj ponownie.")

    def borrow_book(self):
        pass

    def reserve_book(self):
        pass

    def extend_loan(self):
        pass

    def show_all_books(self):
        pass

    def search_by_title(self):
        pass

    def search_by_author(self):
        pass

    def search_by_keywords(self):
        pass

    @staticmethod
    def logout():
        print("Wylogowano użytkownika.")



class EmployeeInterface:
    def __init__(self, library_system):
        self.library_system = library_system

    def run(self):
        while True:
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
        # Implementacja funkcji dodawania nowej książki
        pass

    def remove_book(self):
        # Implementacja funkcji usuwania książki z systemu
        pass

    def add_reader(self):
        # Implementacja funkcji dodawania czytelnika
        pass

    def browse_catalog(self):
        # Implementacja funkcji przeglądania katalogu
        pass

    @staticmethod
    def logout():
        print("Wylogowano pracownika.")

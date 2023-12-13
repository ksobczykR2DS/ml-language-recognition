from filehandler import FileHandler as Fh
from menu import Menu
from security import cipher
from user_options import UserInterface as Ui


class LibrarySystem:
    # z załozenia ten kod bedzie podawany tylko pracownikowi, aby ten mógł założyć konto
    EMPLOYEE_VERIFICATION_CODE = "123"

    # zmienna do przechowywania aktualnego loginu uzytkownika

    def __init__(self):
        self._is_running = True
        self.functions_dict = {
            "1": self._login_to_account,
            "2": self._register_account,
            "3": self._end_app
        }
        self.cipher = cipher.Cipher()

    def _login_to_account(self):
        print("\nLogowanie.")
        login = input("Podaj login (lub wpisz 'end' aby wrócić do menu głównego): ")

        if login.lower() == 'end':
            return  # Wróć do menu głównego
        password = input("Podaj hasło: ")

        user_data = Fh.load_credentials(Fh.USER_DATA)
        employee_data = Fh.load_credentials(Fh.EMPLOYEE_DATA)

        if login in user_data and self.cipher.hash_data(password) == user_data[login]:
            print("Logowanie jako użytkownik udane.")
            Ui.current_user_login = login
            # tu kod dla zalogowanego użytkownika
            user_interface = Ui()
            user_interface.run()
        elif login in employee_data and self.cipher.hash_data(password) == employee_data[login]:
            print("Logowanie jako pracownik udane.")
            # Ue.current_user_login = login
            # tu kod dla zalogowanego pracownika
        else:
            print("Nieprawidłowy login lub hasło. Powrót do menu.")

    def _register_account(self):
        print("\nRejestracja nowego konta:")
        account_type = input("Wybierz rodzaj konta (\"1\" - Użytkownik, \"2\" - Bibliotekarz): ")

        if account_type == "1":
            while True:
                login = input("Podaj login (lub wpisz 'end' aby wrócić do menu głównego): ")

                if login.lower() == 'end':
                    return  # Wróć do menu głównego
                elif Fh.check_login_availability(login, Fh.USER_DATA or Fh.EMPLOYEE_DATA):
                    break
                else:
                    print("Podany login już istnieje. Proszę podać inny login.")
            password = input("Podaj hasło: ")
            hashed_password = self.cipher.hash_data(password)
            Fh.save_credentials(login, hashed_password, Fh.USER_DATA)

        elif account_type == "2":
            verification_code = input("Podaj kod weryfikacyjny: ")
            if verification_code == self.EMPLOYEE_VERIFICATION_CODE:
                print("Kod weryfikacyjny jest poprawny.")
                while True:
                    login = input("Podaj login (lub wpisz 'end' aby wrócić do menu głównego): ")

                    if login.lower() == 'end':
                        return  # Wróć do menu głównego
                    elif Fh.check_login_availability(login, Fh.EMPLOYEE_DATA or Fh.EMPLOYEE_DATA):
                        break
                    else:
                        print("Podany login już istnieje. Proszę podać inny login.")
                password = input("Podaj hasło: ")
                hashed_password = self.cipher.hash_data(password)
                Fh.save_credentials(login, hashed_password, Fh.EMPLOYEE_DATA)
            else:
                print("Nieprawidłowy kod weryfikacyjny. Powrót do menu.")
        else:
            print("Nieprawidłowy wybór rodzaju konta.")

    def _end_app(self) -> None:
        print(f"\nZamykanie programu.")
        self._is_running = False

    def run(self) -> None:
        while self._is_running:
            Menu.show_main_program_menu()
            user_instruction = input("Wybierz opcje: ")
            self._handle_instruction(user_instruction)

    def _handle_instruction(self, user_instruction: str) -> None:
        if user_instruction in self.functions_dict:
            self.functions_dict[user_instruction]()
        else:
            print(f"\nNiewłasciwe polecenie. \"{user_instruction}\" nie jest opcją.\nSpróbuj ponownie\n")

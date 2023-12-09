class Menu:

    @staticmethod
    def show_main_program_menu():
        print("==========================")
        print("[1] Zaloguj się: ")
        print("[2] Zarejestruj się: ")
        print("[3] Zakończ.")
        print("==========================")

    @staticmethod
    def show_main_login_menu():
        print("==========================")
        login = input("Wprowadź login: ")
        password = input("Wprowadź hasło: ")
        print("[1] Zakończ.")
        print("==========================")
        return login, password

    @staticmethod
    def show_new_account_creation_menu():
        pass

class Menu:

    @staticmethod
    def show_main_program_menu():
        print("========================")
        print("[1] Zaloguj się: ")
        print("[2] Zarejestruj się: ")
        print("[3] Zakończ.")
        print("========================")

    @staticmethod
    def show_user_menu():
        print("==========================================================================")
        print("[1] Wypożycz książkę")
        print("[2] Zarezerwuj książkę (jeśli jest wypożyczona)")
        print("[3] Przedłuż wypożyczenie")
        print("[4] Przeglądaj katalogi:")
        print("    [4.1] Wyszukaj po tytule")
        print("    [4.2] Wyszukaj po autorze")
        print("    [4.3] Wyszukaj po słowach kluczowych (np. fantasy, adventure, romance)")
        print("==========================================================================")

    @staticmethod
    def show_employee_menu():
        print("============================")
        print("[1] Przyjmij zwrot książki")
        print("[2] Dodaj nową książkę")
        print("[3] Usuń książkę z systemu")
        print("[4] Dodaj czytelnika")
        print("[5] Przeglądaj katalog")
        print("============================")

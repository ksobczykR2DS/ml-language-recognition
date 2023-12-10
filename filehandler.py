import json


class FileHandler:

    BOOK_DATA = 'security/book_data.json'
    USER_DATA = 'security/user_data.json'
    EMPLOYEE_DATA = 'security/employee_data.json'

    @staticmethod
    def save_credentials(login, password, file_name):
        try:
            with open(file_name, 'r') as is_file:
                data = json.load(is_file)
        except FileNotFoundError:
            data = {}

        data[login] = password

        with open(file_name, 'w') as is_file:
            json.dump(data, is_file, indent=2)

        print(f"Zapisano dane do pliku.")

    @staticmethod
    def load_credentials(file_name):
        try:
            with open(file_name, 'r') as in_file:
                data = json.load(in_file)
                return data
        except FileNotFoundError:
            print(f"Plik {file_name} nie istnieje. Brak danych do odczytu.")
            return {}

    @staticmethod
    def check_login_availability(login, file_name):
        data = FileHandler.load_credentials(file_name)
        if login in data:
            return False
        else:
            return True

    @staticmethod
    def save_books_data(books_data):
        pass

    @staticmethod
    def load_books_data():
        pass
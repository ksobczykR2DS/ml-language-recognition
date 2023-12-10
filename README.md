# JiBAD2023
Języki i Biblioteki Analizy Danych

# Polecenie
Napisać system obsługi biblioteki:
System ma być obsługiwany przez konsolę; gdzie się da, należy użyć menu
System powinien umożliwiać zalogowanie się (jako czytelnik lub bibliotekarz)
Czytelnik może wypożyczyć książkę, zarezerwować książkę, która jest wypożyczona, przedłużyć wypożyczenie, przeglądać
katalog (wyszukiwanie po tytule, autorze lub słowach kluczowych)
Bibliotekarz może przyjąć zwrot książki, dodać nową książkę, usunąć książkę z systemu, dodać czytelnika oraz przeglądać
katalog
System powinien przechowywać swoje dane na dysku (proszę przemyśleć organizację) - zmiany dokonane podczas jednego
uruchomienia programu mają być widoczne w drugim

SYSTEM OBSŁUGI BIBLIOTEKIOKNO 1:
[1] OPCJA LOGOWANIA DO KONTA: UŻYTKOWNIK LUB BIBLIOTEKARZ
[2] OPCJA NOWEGO KONTA: UŻYTKOWNIK LUB BIBLIOTEKARZ
[3] WYJŚCIE

OKNO [1]:
Login:
Password:
Exit:

OKNO [2]:
Menu główne dla Czytelnika:
a. Wypożycz książkę
b. Zarezerwuj książkę (jeśli jest wypożyczona)
c. Przedłuż wypożyczenie
d. Przeglądaj katalogi. Wyszukaj po tytuleii. Wyszukaj po autorzeiii. Wyszukaj po słowach kluczowych
e. Wyloguj się. -> powrót do głównego okna

OKNO [2]: Alternatywa
Menu główne dla Bibliotekarza:
a. Przyjmij zwrot książki
b. Dodaj nową książkę
c. Usuń książkę z systemu
d. Dodaj czytelnika
e. Przeglądaj katalog
f. Wyloguj się. -> powrót to głównego okna

LOGIN: (Każda grupa użytkowników (czytelnicy, bibliotekarze) ma swoje unikalne dane logowania (np. unikalny
identyfikator lub nazwa użytkownika).
Po zalogowaniu się system rozpoznaje, czy użytkownik jest czytelnikiem czy bibliotekarzem i udziela odpowiednich
uprawnień.

ZAPIS PLIKI JSON (szyfrowanie poprzez hashowanie)
Plik 1 -> użytkownicy (hasło, login, ID?)
Plik 2 -> bibliotekarze (hasło, login, ID?)
Plik 3 -> wypożycznia (login, tytuł ksiażki, data, ilość dni)
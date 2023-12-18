# JiBAD2023
Języki i Biblioteki Analizy Danych

# Implementacja KNN przy użyciu Numpy
Zadanie domowe:

Zaimplementować algorytm klasyfikacji binarnej kNN (k najbliższych sąsiadów).
Należy udostępnić metody train i predict.
Train buduje bazę przypadków uczących (przyjmuje przynajmniej wektory i prawidłowe odpowiedzi). Wielokrotne wywołanie metody train powinno rozszerzać zbiór przypadków uczących.
Metoda predict przyjmuje wektor (opcjonalnie: większą liczbę wektorów naraz) i zwraca odpowiedź klasyfikatora.
Należy umożliwić wybór jednej z czterech funkcji odległości: euklidesowej, taksówkowej, maksimum i cosinusowej.

Porównać wyniki na podanych zbiorach dla przynajmniej 3 wartości k (ostatnia kolumna zawiera etykietę).

Pomocna może być metoda np.array.partition.

Termin: 05.01.2024 08:00
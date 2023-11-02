import typing as tp


class InvalidTreeValueError(BaseException):
    pass


class BinarySearchTree:

    def __init__(self, value: int = None):
        self.left = None
        self.right = None
        self.value: int = value

    def insert(self, key: int) -> None:
        if self.value is None:
            self.value = key
        elif self.value == key:
            return
        elif not isinstance(key, int):
            raise InvalidTreeValueError(f"Błąd: Wartość {key} musi być liczbą calkowitą.")
        elif key < self.value:
            if self.left:
                self.left.insert(key)
            else:
                self.left = BinarySearchTree(key)
        else:
            if self.right:
                self.right.insert(key)
            else:
                self.right = BinarySearchTree(key)

    def check_if_exists(self, value: int) -> None:
        if self.value is None:
            print("Brzewo BST jest puste.")
        elif value == self.value:
            print(f"Podana wartość '{value}' istnieje w drzewie BST.")
        elif not isinstance(value, int):
            raise InvalidTreeValueError(f"Błąd: Drzewo nie posiada wartości typu innego niż liczby całkowite.")
        elif value < self.value:
            if self.left:
                self.left.check_if_exists(value)
            else:
                print(f"Podana wartość ('{value}') nie istnieje w drzwie BST.")
        else:
            if self.right:
                self.right.check_if_exists(value)
            else:
                print(f"Podana wartość ('{value}')nie istnieje w drzewie BST.")

    def show_in_order(self) -> tp.List[int]:
        result: tp.List[int] = []
        if self.left:
            result.extend(self.left.show_in_order())
        result.append(self.value)
        if self.right:
            result.extend(self.right.show_in_order())
        return result


def main():
    # Przygotowanie drzewa BST
    nums = [12, 6, -18, 19, 221, 11, 3, -5, 4, 24, 18]
    bst = BinarySearchTree()

    for num in nums:
        try:
            bst.insert(num)
        except InvalidTreeValueError:
            raise InvalidTreeValueError(f"Błąd: Wartość powinna być liczbą całkowitą.")

    # Sprawdzanie, czy wartości istnieją w drzewie
    value_to_check = 9
    bst.check_if_exists(value_to_check)
    value_to_check = -5
    bst.check_if_exists(value_to_check)

    # Wyświetlanie wartości w kolejności rosnącej
    print("Wartości w drzewie BST w kolejności rosnącej:")
    values_in_order = bst.show_in_order()
    print(values_in_order)


if __name__ == "__main__":
    main()

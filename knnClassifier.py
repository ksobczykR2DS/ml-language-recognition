import numpy as np


class KNNClassifier:
    def __init__(self, k, distance):
        self.k = k
        self.distance = distance

    # def compute_distance(self, x):
    #     if self.distance == "euclidean":
    #         return np.sqrt(np.sum())
    #     elif self.distance == "manhattan":
    #         print(2)
    #     elif self.distance == "maximum":
    #         print(3)
    #     elif self.distance == "cosinus":
    #         print(4)

    def train(self, x_train, y_train):
        pass

    def predict(self):
        pass
    
    @staticmethod
    def load_csv(filepath):
        data = np.loadtxt(filepath, delimiter=' ')
        x = data[:, :-1]
        y = data[:, -1]
        return x, y

    @staticmethod
    def get_user_input():
        while True:
            try:
                k = int(input("Podaj liczbę najbliższych sąsiadów k: "))
                if k <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Proszę podać dodatnią liczbę całkowitą.")

        print("Wybierz funkcję obliczania odległości:")
        print("1: Euklidesowa")
        print("2: Manhattan (taksówkowa)")
        print("3: Maksimum")
        print("4: Cosinusowa")
        while True:
            try:
                distance_choice = int(input("Twój wybór (1-4): "))
                if distance_choice not in [1, 2, 3, 4]:
                    raise ValueError
                break
            except ValueError:
                print("Proszę wybrać liczbę od 1 do 4.")

        distance_map = {
            1: 'euclidean',
            2: 'manhattan',
            3: 'maximum',
            4: 'cosine'
        }

        distance = distance_map[distance_choice]
        return k, distance


def main():
    k, distance = KNNClassifier.get_user_input()

    x, y = KNNClassifier.load_csv("data/dataset1.csv")
    classifier = KNNClassifier(k=k, distance=distance)
    classifier.train(x, y)


if __name__ == "__main__":
    main()

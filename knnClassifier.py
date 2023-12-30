import numpy as np
from sklearn.model_selection import train_test_split


class KNNClassifier:
    def __init__(self, k, distance_metric):
        self.k = k
        self.distance_metric = distance_metric
        self.X_train = None
        self.y_train = None

    def fit(self, x_train, y_train):
        self.X_train = x_train
        self.y_train = y_train

    def predict(self, x_train):
        y_pred = [self._predict(sample) for sample in x_train]
        return np.array(y_pred)

    def _predict(self, x):
        distances = np.array([self.distance_metric(x, x_train) for x_train in self.X_train])

        k_indices = np.argpartition(distances, self.k)[:self.k]

        k_nearest_labels = [self.y_train[i] for i in k_indices]
        most_common = np.bincount(k_nearest_labels).argmax()
        return most_common

    def check_prediction(self, x_test, y_test):
        y_pred = self.predict(x_test)
        accuracy = np.mean(y_pred == y_test)
        return accuracy

    @staticmethod
    def compute_euclidean_distance(v1, v2):
        return np.sqrt(np.sum((v1 - v2) ** 2))

    @staticmethod
    def compute_manhattan_distance(v1, v2):
        return np.sum(np.abs(v1 - v2))

    @staticmethod
    def compute_maximum_distance(v1, v2):
        return np.max(np.abs(v1 - v2))

    @staticmethod
    def compute_cosine_distance(v1, v2):
        dot_product = np.dot(v1, v2)
        norm_v1 = np.linalg.norm(v1)
        norm_v2 = np.linalg.norm(v2)
        similarity = dot_product / (norm_v1 * norm_v2)
        return 1 - similarity

    @staticmethod
    def load_data_from_csv(filepath):
        data = []
        labels = []

        with open(filepath, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 3:
                    data.append([float(x) for x in parts[:-1]])
                    labels.append(int(parts[-1]))

        return np.array(data), np.array(labels)

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
            1: KNNClassifier.compute_euclidean_distance,
            2: KNNClassifier.compute_manhattan_distance,
            3: KNNClassifier.compute_maximum_distance,
            4: KNNClassifier.compute_cosine_distance
        }

        distance = distance_map[distance_choice]
        return k, distance


def main():
    print("Wybierz dataset:")
    print("1: dataset0.csv")
    print("2: dataset1.csv")
    print("3: dataset2.csv")
    while True:
        try:
            dataset_choice = int(input("Twój wybór (1-3): "))
            if dataset_choice not in [1, 2, 3]:
                raise ValueError
            break
        except ValueError:
            print("Proszę wybrać liczbę od 1 do 3.")

    dataset_paths = ["data/dataset0.csv", "data/dataset1.csv", "data/dataset2.csv"]
    selected_dataset = dataset_paths[dataset_choice - 1]

    k, distance_metric = KNNClassifier.get_user_input()
    x, y = KNNClassifier.load_data_from_csv(selected_dataset)

    # Podział danych na zbiór treningowy (80%) i testowy (20%)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    classifier = KNNClassifier(k=k, distance_metric=distance_metric)
    classifier.fit(x_train, y_train)

    if len(x_test) == 0:
        print("Zbiór testowy jest pusty. Nie można obliczyć dokładności.")
    else:
        y_pred = classifier.predict(x_test)

        # Obliczenie dokładności klasyfikacji
        accuracy = np.mean(y_pred == y_test)
        print("\nDokładność klasyfikacji:", accuracy)


if __name__ == "__main__":
    main()

from collections import Counter
import string


def read_file_generator(file_path):
    with open(file_path, 'r', encoding='utf-8') as in_file:
        for line in in_file:
            yield line


def count_words(file_path):
    word_counter = Counter()

    for line in read_file_generator(file_path):
        words = line.lower().split()
        words = [word.strip(string.punctuation) for word in words if word and word.strip(string.punctuation)]
        word_counter.update(words)

    return word_counter


def display_top_words(counter, top_words):
    top_values = sorted(set(counter.values()), reverse=True)[:top_words]

    for i, value in enumerate(top_values, start=1):
        matching_items = [(key, count) for key, count in counter.items() if count == value]
        print(f"(Place {i}):")
        for key, count in matching_items:
            print(f"{key}: {count} occurrences")


def main():
    word_results = count_words('potop.txt')
    display_top_words(word_results, 5)


if __name__ == '__main__':
    main()

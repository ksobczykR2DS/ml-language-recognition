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
    sorted_words = counter.most_common(top_words)

    print(f"Top {top_words} words: ")
    for i, (word, count) in enumerate(sorted_words, start=1):
        print(f"{i}. {word}: {count} occurrences")

    # print(f"Top {top_words} words occurrences: ")
    # for i, (word, count) in enumerate(sorted_words, start=1):
    #     matching_items = [(word, count) for word, count in sorted_words if count == count]
    #     print(f"Words with count {count} (Place {i}): ")
    #     for word, count in matching_items:
    #         print(f"{word}: {count} occurrences")


def main():
    word_results = count_words('potop.txt')
    display_top_words(word_results, 5)


if __name__ == '__main__':
    main()

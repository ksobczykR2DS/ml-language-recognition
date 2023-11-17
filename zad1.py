from collections import Counter


def count_words(file_path):
    word_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as in_file:
        for line in in_file:
            words = line.lower().split()
            word_counter.update(words)

    return word_counter


def display_top_words(counter, top_words):
    sorted_words = sorted(set(count_words(file_path='potop.txt')), reverse=True)[:top_words]

    print(f"Top {top_words} words: ")
    for i, (word, count) in enumerate(sorted_words[:top_words], start=1):
        matching_items = [(word, count) for word, count in sorted_words if count == counter]
        print(f"\nWords with count {count} (Place {i}): ")
        for word, count in matching_items:
            print(f"{word}: {count} occurrences")


def main():
    word_results = count_words('potop.txt')
    display_top_words(word_results, 5)


if __name__ == '__main__':
    main()

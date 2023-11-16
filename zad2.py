from collections import Counter


def count_ngrams(file_path, n):
    ngram_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as in_file:
        for line in in_file:
            words = line.lower().split()
            ngrams = (tuple(words[i:i + n]) for i in range(len(words) - n + 1))
            ngram_counter.update(ngrams)

        return ngram_counter


def display_top_ngrams(counter, top_n):
    top_values = sorted(set(counter.values()), reverse=True)[:3]

    for i, value in enumerate(top_values, start=1):
        matching_items = [(key, count) for key, count in counter.items() if count == value]
        print(f"\nPairs with value {value} (Place {i}):")
        for key, count in matching_items:
            print(f"{key}: {count} occurrences")


def main():
    ngram_results = count_ngrams('szymborska.txt', 3)
    print(ngram_results)
    display_top_ngrams(ngram_results, 3)


if __name__ == '__main__':
    main()

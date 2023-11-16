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
    top_ngrams = counter.most_common(top_n)

    print(f"Top {top_n} n-grams:")
    for ngram, count in top_ngrams:
        print(f"{ngram}: {count} occurrences")


def main():
    ngram_results = count_ngrams('szymborska.txt', 3)
    display_top_ngrams(ngram_results, 3)


if __name__ == '__main__':
    main()

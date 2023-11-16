from collections import Counter


def display_top_engrams(file_path, n):
    ngram_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as in_file:
        for line in in_file:
            words = line.lower().split()
            ngrams = [words[i:i + n] for i in range(len(words) - n + 1)]
            ngram_counter.update(ngrams)

        return ngram_counter


def count_ngrams():
    pass


def main():
    pass


if __name__ == '__main__':
    main()

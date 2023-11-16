class ConllContextManager:
    def __init__(self, filename, encoding):
        self.filename = filename
        self.encoding = encoding

    def __enter__(self):
        self.file = open(self.filename, 'r', encoding='utf-8')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

    def __iter__(self):
        return self

    def __next__(self):
        for line in self.file:
            if not line.isspace():
                parts = [element.strip('"') for element in line.strip().split('\t')]
                words = [word.strip('"') for word in parts[0].split(' ')]
                return tuple(words)
        raise StopIteration


with ConllContextManager('nkjp.conll', encoding='utf-8') as in_file:
    for token in in_file:
        print(token)

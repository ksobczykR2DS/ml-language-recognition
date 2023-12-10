import hashlib


class Cipher:
    def __init__(self, algorithm='sha256'):
        self.algorithm = algorithm

    def hash_data(self, data):
        if isinstance(data, str):
            data = data.encode('utf-8')

        hash_algorithm = hashlib.new(self.algorithm)
        hash_algorithm.update(data)

        return hash_algorithm.hexdigest()

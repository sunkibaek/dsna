import hashlib
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


def main():
    block_1 = Block(datetime.datetime.now(), "test data 1", None)
    block_2 = Block(datetime.datetime.now(), "test data 2", block_1)
    block_3 = Block(datetime.datetime.now(), "test data 3", block_2)

    print(block_1.hash)
    print(block_2.hash)
    print(block_3.hash)


main()

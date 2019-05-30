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


def test1():
    block_1 = Block(datetime.datetime.now(), "test data 1", None)
    block_2 = Block(datetime.datetime.now(), "test data 2", block_1.hash)

    print(block_1.hash == block_2.previous_hash)
    # True


def test2():
    block_1 = Block(datetime.datetime.now(), "test data 1", None)
    block_2 = Block(datetime.datetime.now(), "test data 2", block_1.hash)
    block_3 = Block(datetime.datetime.now(), "test data 3", block_2.hash)

    print(block_1.hash == block_2.previous_hash)
    # True
    print(block_2.hash == block_3.previous_hash)
    # True


def test3():
    block_1 = Block(datetime.datetime.now(), "test data 1", None)

    print(block_1.hash)
    # 05e8fdb3598f91bcc3ce41a196e587b4592c8cdfc371c217274bfda2d24b1b4e


test1()
test2()
test3()

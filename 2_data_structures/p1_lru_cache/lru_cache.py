class LRU_Cache(object):

    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.cache_keys = [None for _ in range(capacity)]

    def get(self, key):
        if self.cache.get(key) != None:
            return self.cache.get(key)

        return -1

    def set(self, key, value):
        if len(self.cache_keys) == self.capacity:
            oldest_key = self.cache_keys.pop()
            self.cache[oldest_key] = None

        if self.cache.get(key) == None:
            self.cache[key] = value
            self.cache_keys.insert(0, key)


def test(case, received, expected):
    if expected != received:
        print(case + " fail - expected: " + str(expected) +
              ", received: " + str(received))
        return

    print(case + " pass")


def test_case_1():
    print("====================")
    print("Regular cache usage")
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)

    test("For 1, cache hit", our_cache.get(1), 1)
    test("For 2, cache hit", our_cache.get(2), 2)
    test("For 3, cache miss", our_cache.get(3), -1)


def test_case_2():
    print("====================")
    print("Over capacity cache usage")
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.set(5, 5)
    our_cache.set(6, 6)

    test("For 5, cache hit", our_cache.get(5), 5)
    test("For 6, cache hit", our_cache.get(6), 6)
    test("For 1, cache miss", our_cache.get(1), -1)


def main():
    test_case_1()
    test_case_2()


main()

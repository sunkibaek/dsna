class LRU_Cache(object):

    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.cache_keys = [None for _ in range(capacity)]

    def get(self, key):
        if self.cache.get(key) != None:
            self.move_cache_key_to_front(key)

            return self.cache.get(key)

        return -1

    def set(self, key, value):
        if len(self.cache_keys) == self.capacity:
            oldest_key = self.cache_keys.pop()
            self.cache[oldest_key] = None

        if self.cache.get(key) == None:
            self.cache[key] = value
            self.cache_keys.insert(0, key)

    def move_cache_key_to_front(self, key):
        self.cache_keys.insert(
            0, self.cache_keys.pop(self.cache_keys.index(key)))


def test(case, received, expected):
    if expected != received:
        print(case + " fail - expected: " + str(expected) +
              ", received: " + str(received))
        return

    print(case + " pass")


def test_case_1():
    print("====================")
    print("When data is not stored in cache")
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)

    test("For 1, cache hit", our_cache.get(1), 1)
    # For 1, cache hit pass
    test("For 2, cache hit", our_cache.get(2), 2)
    # For 2, cache hit pass
    test("For 3, cache miss", our_cache.get(3), -1)
    # For 3, cache miss pass


def test_case_2():
    print("====================")
    print("When max capacity reached - default order")
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.set(5, 5)
    our_cache.set(6, 6)

    test("For 5, cache hit", our_cache.get(5), 5)
    # For 5, cache hit pass
    test("For 6, cache hit", our_cache.get(6), 6)
    # For 6, cache hit pass
    test("For 1, cache miss", our_cache.get(1), -1)
    # For 1, cache miss pass


def test_case_3():
    print("====================")
    print("Over max capacity reached - least used")
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.set(5, 5)

    test("For 1, cache hit", our_cache.get(1), 1)
    # For 1, cache hit pass
    test("For 3, cache hit", our_cache.get(3), 3)
    # For 3, cache hit pass
    test("For 4, cache hit", our_cache.get(4), 4)
    # For 4, cache hit pass
    test("For 5, cache hit", our_cache.get(5), 5)
    # For 5, cache hit pass

    our_cache.set(6, 6)
    test("For 2, cache miss", our_cache.get(2), -1)
    # For 2, cache miss pass


test_case_1()
test_case_2()
test_case_3()

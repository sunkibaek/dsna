import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = None
    max = None

    # iterating the list in O(n)
    for i in ints:
        if min == None or min > i:
            min = i

        if max == None or max < i:
            max = i

    return min, max

# Example Test Case of Ten Integers


def test_function(actual, expect):
    if actual[0] == expect[0] and actual[1] == expect[1]:
        print("Pass")
    else:
        print("Fail", actual, expect)


l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

test_function(get_min_max(l), (0, 9))

test_function(get_min_max([0, 1]), (0, 1))

test_function(get_min_max([1, 9]), (1, 9))

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    sorted_list = [None for _ in range(len(input_list))]
    counts = {
        0: 0,
        1: 0,
        2: 0
    }

    for index, element in enumerate(input_list):
        if element == 0:
            if sorted_list[counts[0]] == 1:
                sorted_list[counts[0]] = 0
                sorted_list[counts[0] + counts[1]] = 1
            else:
                sorted_list[counts[0]] = 0

        if element == 1:
            sorted_list[counts[0] + counts[1]] = 1

        if element == 2:
            sorted_list[len(input_list) - 1 - counts[2]] = 2

        counts[element] += 1

    return sorted_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

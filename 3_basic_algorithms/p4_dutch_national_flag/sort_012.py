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
        # fill the list from left for 0
        if element == 0:
            # if 0 spill into 1 move 1 to right by 1
            if sorted_list[counts[0]] == 1:
                sorted_list[counts[0]] = 0
                sorted_list[counts[0] + counts[1]] = 1
            else:
                sorted_list[counts[0]] = 0

        # fill the list after 0 for 1
        if element == 1:
            sorted_list[counts[0] + counts[1]] = 1

        # fill the list from right for 2
        if element == 2:
            sorted_list[len(input_list) - 1 - counts[2]] = 2

        counts[element] += 1

    return sorted_list


def test_function(test_case):
    sorted_array = sort_012(test_case)

    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail", sorted_array)


# regular case
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])

# regular case
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])

# regular case
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

# already sorted
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# minimum case
test_function([2, 1, 0])

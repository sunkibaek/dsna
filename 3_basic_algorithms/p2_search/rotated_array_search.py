def binary_search(input_list, number, index_offset):
    start_index = 0
    end_index = len(input_list) - 1
    mid_index = (start_index + end_index) // 2

    while True:
        if number == input_list[mid_index]:
            return mid_index + index_offset

        if mid_index == 0 or mid_index == len(input_list) - 1:
            break

        if number > input_list[mid_index]:
            mid_index = (end_index + mid_index + 1) // 2
            continue

        if number < input_list[mid_index]:
            mid_index = (start_index + mid_index) // 2
            continue

        break

    return -1


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start_index = 0
    end_index = len(input_list) - 1
    rotate_index = 0

    # find rotated index: O(n)
    for index, element in enumerate(input_list):
        if index > 0 and input_list[index] < input_list[index - 1]:
            rotate_index = index
            break

    # compare what section the number belongs: O(1)
    # set boundaries
    if number >= input_list[0] and number <= input_list[rotate_index - 1]:
        end_index = rotate_index - 1
    elif number >= input_list[rotate_index] and number <= input_list[len(input_list) - 1]:
        start_index = rotate_index

    # binary search within boundaries: O(log n)
    return binary_search(input_list[start_index:(end_index + 1)], number, start_index)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# search an element of the first section
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])

# search an element of the second section
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])

# search an element that does not exist
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# search an element from minimum set
test_function([[6, 1], 6])

# search an element from minimum set
test_function([[6, 1], 1])

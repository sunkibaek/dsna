def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    lower_index = 0
    upper_index = len(input_list) - 1
    mid_index = (lower_index + upper_index) / 2
    start_index = lower_index
    end_index = upper_index

    if input_list[lower_index] == number:
        return lower_index
    if input_list[mid_index] == number:
        return mid_index
    if input_list[upper_index] == number:
        return upper_index

    if input_list[lower_index] < number and input_list[mid_index] > number:
        start_index = lower_index
        end_index = mid_index
    elif input_list[mid_index] < number and input_list[upper_index] > number:
        start_index = mid_index
        end_index = upper_index
    elif input_list[upper_index] > number and input_list[mid_index] > number:
        start_index = mid_index
        end_index = upper_index

    search_index = (start_index + end_index) / 2
    count = 0

    while not input_list[search_index] == number:
        count += 1

        if input_list[search_index] < number:
            search_index = (search_index + end_index) / 2
        else:
            search_index = (search_index + start_index) / 2

    print(count)

    return search_index


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


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

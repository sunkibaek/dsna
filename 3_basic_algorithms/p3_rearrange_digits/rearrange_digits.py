def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # sort the list in O(n log n)
    sorted_list = sorted(input_list, reverse=True)
    first = ""
    second = ""

    # assign an element to first or second section alternatively
    # O(n)
    for index, element in enumerate(sorted_list):
        if index % 2:
            second += str(element)
        else:
            first += str(element)

    return [int(first), int(second)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail", output, solution)


# regular case
test_function([[1, 2, 3, 4, 5], [542, 31]])

# regular case
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# regular case
test_function([[1, 2, 3, 4, 5, 6, 7, 8, 9], [97531, 8642]])

# test for minimum input
test_function([[1, 2], [1, 2]])

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    upper_bound = number
    lower_bound = 1
    candidate = upper_bound

    if number ** 2 == number:
        return number

    while True:
        if upper_bound - lower_bound == 1:
            return lower_bound

        half = candidate // 2

        if half ** 2 > number:
            upper_bound = half
            candidate = upper_bound

            continue
        elif half ** 2 < number:
            lower_bound = half
            candidate = upper_bound + lower_bound

            continue
        else:
            return half


def test(result, expect):
    """
    print Pass for success, Fail with result and expect for failure
    """
    if result == expect:
        print("Pass")
    else:
        print("Fail", result, expect)


# regular case
# 9 -> 3
test(sqrt(9), 3)

# regular case
# 16 -> 4
test(sqrt(16), 4)

# does it floor?
# 27 -> 5
test(sqrt(27), 5)

# edge case
# 0 -> 0
test(sqrt(0), 0)

# edge case
# 1 -> 1
test(sqrt(1), 1)

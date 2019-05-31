"""
If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose
floor value is 5.

The expected time complexity is O(log(n))
"""


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

        half = candidate / 2

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


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

print("Pass" if (1 == sqrt(2)) else "Fail")

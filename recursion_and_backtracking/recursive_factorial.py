number = int(input())


def recursion_find_factorial(factorial):
    if factorial <= 1:
        return 1
    return factorial * recursion_find_factorial(factorial -1)


print(recursion_find_factorial(number))

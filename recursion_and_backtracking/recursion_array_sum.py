numbers = [int(num) for num in input().split()]
index = len(numbers) - 1


def recursion_sum(array, idx):
    if idx <= 0:
        return array[idx]
    return array[idx] + recursion_sum(array, idx - 1)


print(recursion_sum(numbers, idx=index))

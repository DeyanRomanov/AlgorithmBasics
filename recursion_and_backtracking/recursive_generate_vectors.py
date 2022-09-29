length_of_vector = int(input())
base_vector = [None] * length_of_vector

start_index = 0

'''
    Generate all n-bit vectors of 0 and 1 in lexicographic order.
'''


def recursive_generating_vectors(vector, index):
    if len(vector) <= index:
        return print(*vector)
    for x in range(2):
        vector[index] = x
        recursive_generating_vectors(vector, index + 1)


recursive_generating_vectors(base_vector, start_index)

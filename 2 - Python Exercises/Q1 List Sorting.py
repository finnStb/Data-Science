# Q1: Write 2 python function to get the indices of the sorted elements of given lists and compare the speed.
# one is without numpy package and the other is with numpy.
# (raise a error message if the input is null or not numerical) -- 13pt
#
# List 1: [23, 104, 5, 190, 8, 7, -3]
# List 2 : []
# List 3 : random generate 1000000 integers

import numpy as np
import time


def sort_list(list_1):
    if not list_1:
        raise ValueError("List is empty")
    for i in list_1:
        if not isinstance(i, int):
            raise ValueError("List contains non-integer values")
    return sorted(range(len(list_1)), key=lambda x: list_1[x])


def sort_list_numpy(list_1):
    if not list_1:
        raise ValueError("List is empty")
    for i in list_1:
        if not isinstance(i, int):
            raise ValueError("List contains non-integer values")
    return np.argsort(list_1)


list1 = [23, 104, 5, 190, 8, 7, -3]
list2 = []
list3 = [int(i) for i in np.random.randint(low=0, high=np.iinfo(np.int32).max, size=1000000)]

start = time.time()
sort_list(list1)
print("Time taken without numpy: ", time.time() - start)  # 0.0
start = time.time()
sort_list_numpy(list1)
print("Time taken with numpy: ", time.time() - start)  # 0.001

# Conclusion: Numpy is slower for very small lists.

start = time.time()
sort_list(list3)
print("Time taken without numpy: ", time.time() - start)  # 0.91
start = time.time()
sort_list_numpy(list3)
print("Time taken with numpy: ", time.time() - start)  # 0.20

# Conclusion: Numpy is faster for large lists.

start = time.time()
sort_list(list2)
print("Time taken without numpy: ", time.time() - start)  # ValueError: List is empty
start = time.time()
sort_list_numpy(list2)
print("Time taken with numpy: ", time.time() - start)  # ValueError: List is empty

# no conclusion can be drawn for empty lists.




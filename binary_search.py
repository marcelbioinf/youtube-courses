import random
import time

def naive_search_v1(l, target):
    for i, item in enumerate(l):
        if item == target:
            return l[i]
    return -1


def naive_search_v2(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


def binary_search(list, target, low=None, high=None):  # binary search should be faster, it uses divide and conquer!

    if low is None:
        low = 0
    if high is None:
        high = len(list) - 1

    if high < low:
        return -1

    middle_value_index = (low + high) // 2

    if list[middle_value_index] == target:
        return middle_value_index
    elif target < list[middle_value_index]:
        return binary_search(list, target, low, middle_value_index - 1)
    else:
        return binary_search(list, target, middle_value_index + 1, high)

length = 10000
sorted_list = set()
while len(sorted_list) < length:
    sorted_list.add(random.randint(-3*length, 3*length))
sorted_list = sorted(list(sorted_list))

#target = random.randint(-3*length, 3*length)

start = time.time()
for target in sorted_list:
    naive_search_v1(sorted_list, target)
end = time.time()
print(f'Naive search v1: {(end-start)/length} seconds per one iteration')

start = time.time()
for target in sorted_list:
    naive_search_v2(sorted_list, target)
end = time.time()
print(f'Naive search v2: {(end-start)/length} seconds per one iteration')

start = time.time()
for target in sorted_list:
    binary_search(sorted_list, target)
end = time.time()
print(f'Bonary search: {(end-start)/length} seconds per one iteration')


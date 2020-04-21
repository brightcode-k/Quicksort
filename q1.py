from random import randint


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        #elems that are higher than pivot
        while low <= high and array[high] >= pivot:
            high = high - 1
        #elems that are lower than pivot
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def quick_sort(array, start, end):
    if start >= end:
        return None
    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

def generator():
    l1 = list()
    n = int(input("Len array: "))
    for i in range(n):
        i += 1
        l1.append(randint(0, 50))
        if i > n:
            break
    return l1
array = generator()
print(array)
quick_sort(array, 0, len(array) - 1)
print("\n", array)
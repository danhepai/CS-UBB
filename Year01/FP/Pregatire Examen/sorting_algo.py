"""
Algos:

1. BubbleSort
2. InsertionSort
3. SelectionSort
4. MergeSort: Iterative + Recursive
5. QuickSort: Iterative + Recursive

Bonus:
6. BinarySearch: Iterative + Recursive
"""


def binarySearchIterative(arr, element):
    """
    Search the element 'element' in the list 'arr'.
    :return: position if founded, -1 otherwise
    """
    if len(arr) == 0 or element <= arr[0]:
        return 0

    if element > arr[len(arr) - 1]:
        return len(arr)

    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if element == arr[middle]:
            return middle
        elif element < arr[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return left


def binarySearchRecursive(arr, left, right, element):
    if len(arr) == 0:
        return False, 0

    if left > right:
        return False, left

    middle = (left + right) // 2
    if element == arr[middle]:
        return True, middle
    if element > arr[middle]:
        return binarySearchRecursive(arr, middle + 1, right, element)
    if element < arr[middle]:
        return binarySearchRecursive(arr, left, middle - 1, element)


def merge(arr_one, arr_two):
    merged_list = []

    i, j = 0, 0
    while i < len(arr_one) and j < len(arr_two):
        if arr_one[i] < arr_two[j]:
            merged_list.append(arr_one[i])
            i += 1
        else:
            merged_list.append(arr_two[j])
            j += 1

    while i < len(arr_one):
        merged_list.append(arr_one[i])
        i += 1

    while j < len(arr_two):
        merged_list.append(arr_two[j])
        j += 1

    return merged_list


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = mergeSort(arr[:middle])
    right = mergeSort(arr[middle:])
    return merge(left, right)


def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr.pop()
    lesser = quickSort([x for x in arr if x <= pivot])
    greater = quickSort([x for x in arr if x > pivot])
    return lesser + [pivot] + greater


def oneLinerQuickSort(arr):
    return arr if len(arr) <= 1 else oneLinerQuickSort([x for x in arr[1:] if x <= arr[0]]) + [
        arr[0]] + oneLinerQuickSort([x for x in arr[1:] if x > arr[0]])


def DirectSelectionSort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


def partition(arr, left, right):
    pivot = arr[right]
    i = left
    j = right - 1
    while i < j:
        while arr[i] <= pivot and i < right:
            i += 1
        while arr[j] > pivot and j > left:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


def quickSortWithPartition(arr, left, right):
    if left < right:
        pivot_pos = partition(arr, left, right)
        quickSortWithPartition(arr, left, pivot_pos - 1)
        quickSortWithPartition(arr, pivot_pos + 1, right)

def BubbleSort(arr):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                isSorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


def SelectionSort(arr):
    for i in range(len(arr) - 1):
        ind = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[ind]:
                ind = j
        arr[i], arr[ind] = arr[ind], arr[i]


def InsertionSort(arr):
    for i in range(1, len(arr)):
        ind = i - 1
        el = arr[i]
        while ind >= 0 and el < arr[ind]:
            arr[ind + 1] = arr[ind]
            ind -= 1
        arr[ind + 1] = el


if __name__ == '__main__':
    arr = [9, 8, 7, 6, 1, 2, 3, 4, 7, 55, 66, 1]
    arr2 = [1,2,3,4]
    quickSortWithPartition(arr, 0, len(arr) - 1)
    print(arr)

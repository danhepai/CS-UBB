def compareMovies(x, y):
    if x.getTitle() == y.getTitle() and x.getDescription() < y.getDescription():
        return x.getType() < y.getType()
    if x.getTitle() == y.getTitle():
        return x.getDescription() < y.getDescription()
    return x.getTitle() < y.getTitle()


def insertion_sort(arr, key=lambda x: x, cmp=lambda x, y: x < y, reverse=False):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and cmp(key(arr[j]), key(arr[j - 1])):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    if reverse:
        arr.reverse()
    return arr


def quickSort(arr, key=lambda x: x, cmp=lambda x, y: x < y, reverse=False):
    if len(arr) <= 1:
        return arr
    pivot = arr.pop()
    lesser = quickSort([x for x in arr if cmp(key(x), key(pivot))])
    greater = quickSort([x for x in arr if not cmp(key(x), key(pivot))])
    if reverse:
        return (lesser + [pivot] + greater).reverse()


def get_next_gap(gap):
    gap = (gap * 10) / 13
    if gap < 1:
        return 1
    return int(gap)


def comb_sort(arr, key=lambda x: x, cmp=lambda x, y: x < y, reverse=False):
    n = len(arr)
    gap = n
    swapped = True
    while gap != 1 or swapped == 1:
        gap = get_next_gap(gap)
        swapped = False
        for i in range(0, n - gap):
            if cmp(key(arr[i]), key(arr[i + gap])):
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    if reverse:
        arr.reverse()
    return arr

def quicksort(arr):
    less = []
    more = []
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        for i in arr[1:]:
            if i <= pivot:
                less.append(i)
            else:
                more.append(i)
        return quicksort(less) + [pivot] + quicksort(more)

print(quicksort([10, 5, 22, 1952, 2, 3]))

def quicksortTwo(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        more = [i for i in arr[1:] if i > pivot]
        return quicksortTwo(less) + [pivot] + quicksortTwo(more)

print(quicksortTwo([10, 5, 22, 1952, 2, 3]))

                
def FindSmallest(arr):
    smallest = arr[0];
    smallest_index=0;
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def Selection_Sort(arr):
    newArr = [];
    for i in range(len(arr)):
        smallest = FindSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(Selection_Sort([5, 3, 6, 2, 10]))
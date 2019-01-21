def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while (low <= high):
        # while the guess is not narrowed down to one element
        mid = (low + high)/2
        # Check the middle element
        guess = list[mid]
        if guess == item:
            # guess is the item we are looking for
            return mid
        elif guess > item:
            # the guess was too high and we narrow the focus to mid - 1
            high = mid - 1
        else:
            # the guess was too low and we narrow the focus to mid + 1
            low = mid + 1
            # Item doesn't exist...
    return None

print("running binary.py")
my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
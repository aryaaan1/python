arr = [9, 4, 7, 4, 2, 9, 4, 1]

low = 0
mid = 0
high = len(arr) - 1

pivot = 4

while mid <= high:

    if arr[mid] < pivot:
        arr[low], arr[mid] = arr[mid], arr[low]
        low = low + 1
        mid = mid + 1

    elif arr[mid] == pivot:
        mid = mid + 1

    else:
        arr[mid], arr[high] = arr[high], arr[mid]
        high = high - 1

print(arr)
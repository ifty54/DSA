def sort_num(arr):
    n = len(arr)
    low, mid, high = 0, 0, n-1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

arr = [2,0,1,0,2,1]
print(sort_num(arr))

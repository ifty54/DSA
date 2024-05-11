def find_min_max(arr):
    n = len(arr)
    
    if n % 2 == 0:
        if arr[0] > arr[1]:
            max = arr[0]
            min = arr[1]
        else:
            min = arr[0]
            max = arr[1]
        start_index = 2
    else:
        min = arr[0]
        max = arr[0]
        start_index = 1
    
    for i in range(start_index, n-1, 2):
        if arr[i] > arr[i+1]:
            if arr[i] > max:
                max = arr[i]
    
            if arr[i+1] < min:
                min = arr[i+1]
        else:
            if arr[i+1] > max:
                max = arr[i+1]
                
            if arr[i] < min:
                min = arr[i]
    return min, max
        
arr = [5,2,10,7,5,9]
min, max = find_min_max(arr)
print("min element: ", min)
print("max element: ", max)

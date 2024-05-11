def merge_sorted_arrays(arr1, arr2):
    p1 = p2 = 0
    merged_arr = []

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            merged_arr.append(arr1[p1])
            p1 += 1
        else:
            merged_arr.append(arr2[p2])
            p2 += 1

    merged_arr.extend(arr1[p1:])
    merged_arr.extend(arr2[p2:])

    return merged_arr


arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merged_arr = merge_sorted_arrays(arr1, arr2)
print("Merged sorted array:", merged_arr)

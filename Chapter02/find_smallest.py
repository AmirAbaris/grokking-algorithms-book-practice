def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range (1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    
    return smallest_index


def section_sort(arr):
    new_arr = []
    copiedArr = list(arr)
    for i in range(len(copiedArr)):
        smallest = find_smallest(copiedArr)
        new_arr.append(copiedArr.pop(smallest))
    
    return new_arr

print(section_sort([5, 3, 6, 2, 10]))
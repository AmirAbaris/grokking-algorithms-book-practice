def quick_sort(arr):
    # if array len is 0 or 1
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        lesser_elements = [i for i in arr[:-1] if i <= pivot]
        greater_elements = [i for i in arr[:-1] if i > pivot]
        return quick_sort(lesser_elements) + [pivot] + quick_sort(greater_elements)

print(quick_sort([55, 45, 33, 26, 2, 5,]))
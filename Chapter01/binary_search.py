# for binary search we need to sort the list
# if the list is not sorted then we can sort it using sorted() function

# and our lower bound will be 0
# and our upper bound will be len(list) - 1
# note: we dont need the last index for sorting the upper bound!

# and the middle will be (lower_bound + upper_bound) // 2
# note: middle is gonna be rounded by python if it is an odd number

# and fist we need a input to start our search
# we need to start the search from the middle of the list

# and if the guess is too low we need to increase the lower bound
# and if the guess is too high we need to decrease the upper bound

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

my_list = [1, 3, 5, 7, 9]
        
print(binary_search(my_list, 3)) # => 1
print(binary_search(my_list, -1)) # => None


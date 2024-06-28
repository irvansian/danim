import sorting
def linear_search(arr, x):
    for i in range(0, len(arr)):
        if arr[i] == x:
            return i


# best searching algorithm for sorted list
def binary_search(arr, x):
    if len(arr) == 0:
        return False
    if len(arr) == 1:
        return arr[0] == x
    mid = len(arr) // 2
    if arr[mid] == x:
        return True
    elif arr[mid] > x:
        return binary_search(arr[:mid], x)
    else:
        return binary_search(arr[mid + 1:], x)




example_array = [34, 7, 23, 32, 5, 62, 12]
sorted_array = sorting.insertion_sort_inc(example_array)
print('sorted array ' + str(sorted_array))
result = binary_search(sorted_array, 7)
print(result)

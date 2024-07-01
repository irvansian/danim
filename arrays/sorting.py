#incremental method
def insertion_sort_inc(array):
    n = len(array)
    for i in range(1, n - 1):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array


#incremental method
def insertion_sort_dec(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

    return arr


#incremental method
def selection_sort(arr, n):
    for i in range(0, n):
        smallest_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        temp = arr[smallest_index]
        arr[smallest_index] = arr[i]
        arr[i] = temp

    return arr


'''
User divide and conquer.
Divide -> the problems into smaller problems
Conquer -> the subproblem by solving them recursively
Combine -> the solution of the subproblems
'''


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    first = arr[0: mid]  #can also write arr[:mid]
    second = arr[mid: len(arr)]  #can also write arr[mid:]

    first_sorted = merge_sort(first)
    second_sorted = merge_sort(second)

    sorted = []  #this is like having 2 sorted card decks, we take the smallest card from both deck
    i = 0  #iterator for first_sorted
    j = 0  #iterator for second_sorted

    while i < len(first_sorted) and j < len(second_sorted):
        if (first_sorted[i] <= second_sorted[j]):
            sorted.append(first_sorted[i])
            i += 1
        else:
            sorted.append(second_sorted[j])
            j += 1

    sorted = sorted + second_sorted[j:]
    sorted = sorted + first_sorted[i:]

    return sorted


example_array = [34, 7, 23, 32, 5, 62, 12]
sorted_array = merge_sort(example_array)
print(sorted_array)
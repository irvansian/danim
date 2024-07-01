"""
TEMPLATE BACKTRACKING:
given args : list or iterable items

1. list to save results
2. params usually
   1. curPath
   2. remaining options/index of iterable list
   3. (optional) state variables of current recursion stack
3. blocks usually
   1. saving curPath (may/may not be inside the base case)
   2. base_case to return (not necessary if we exhaust the iterable items)
   3. (POLICY) looping over valid remaining options


results = []

def backtrack(params):
    # here we can also save curPath if needed all results with various length
    if base_case:
        results.append(curPath)
        return

    for option in remaining_options:
        if option not valid:
            continue

        curPath.append(option)
        backtrack(curPath, modified_remaining_options)
        curPath.pop()
"""


def subsets(arr):
    """
    SUBSET (original)
    """
    results = []

    def backtrack(cur_set, start):
        results.append(cur_set[:])

        # here we don't need base case that
        # returns since it runs to exhaust the list

        for i in range(start, len(arr)):
            cur_set.append(arr[i])
            backtrack(cur_set, i + 1)
            cur_set.pop()

    backtrack([], 0)

    return results


def permute(arr):
    """
    PERMUTATION (original)
    :param arr:
    :return:
    """
    results = []

    def backtrack(curPath, used):
        if len(curPath) == len(arr):
            results.append(curPath[:])
            return

        for item in arr:
            if item in used:
                continue

            used.add(item)
            curPath.append(item)
            backtrack(curPath, used)
            curPath.pop()
            used.remove(item)

    backtrack([], set())

    return results


def combine(n, k):
    """
    SUBSET (of length k)
    :param n:
    :param k:
    :return:
    """
    results = []

    def backtrack(curComb, start):
        if len(curComb) == k:
            results.append(curComb[:])
            return

        for num in range(start, n + 1):
            curComb.append(num)
            backtrack(curComb, num + 1)
            curComb.pop()

    backtrack([], 1)
def longestArrayNoRepeat(arr):
    """
    ORIGINAL VARIABLE SIZED SLIDING WINDOW (MAXIMAL)
    :param arr:
    :return:
    """
    l = r = 0
    maxLength = 0
    seen = set()

    while r < len(arr):
        while arr[r] in seen:
            seen.remove(arr[l])
            l += 1

        seen.add(arr[r])
        maxLength = max(maxLength, r - l + 1)
        r += 1

    return maxLength


def minimumSubarraySum(nums, target):
    """
    ORIGINAL VARIABLE SIZED SLIDING WINDOW (MINIMAL)
    :param nums:
    :param target:
    :return:
    """

    l = r = 0
    minSum = float('inf')
    curSum = 0

    while r < len(nums):
        curSum += nums[r]

        while curSum >= target:
            minSum = min(minSum, curSum)
            curSum -= nums[l]
            l += 1

        r += 1

    return minSum if minSum != float('inf') else 0


def maxSubarrayAvg(arr, k):
    """
    ORIGINAL FIXED SIZE SLIDING WINDOW (MAX & MIN sama aja)
    1. do something with the first k subarray
    2. initialize l = 1, r = k
    3. block: (a) update curVar with arr[k] and arr[l - 1]
              (b) slide window (increment l and r)
              (c) update maxVar or minVar
    :param arr:
    :param k:
    :return:
    """
    curSum = sum(arr[:k])
    maxSum = curSum

    l = 1
    r = k

    while r < len(arr):
        curSum += arr[r] - arr[l]
        l += 1
        r += 1
        maxSum = max(maxSum, curSum)

    return maxSum / float(k)


def bestBuySellStock(prices):
    """
    FIND MIN AND MAX WHERE INDEX(MIN) < INDEX(MAX)
    similar to kadane's algorithm
    :param prices:
    :return:
    """
    if len(prices) == 1:
        return 0

    minPrice = float('inf')
    maxProfit = 0

    for price in prices:
        maxProfit = max(maxProfit, price - minPrice)
        minPrice = min(minPrice, price)

    return maxProfit
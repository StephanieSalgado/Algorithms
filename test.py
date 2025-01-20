import random

def find_max_crossing_subarray(arr, low, mid, high):
    left_sum = float("-inf")
    sum = 0
    max_left = 0
    for i in range(mid, low - 1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = float("-inf")
    sum = 0
    max_right = 0
    for j in range(mid + 1, high + 1):
        sum += arr[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return (max_left, max_right, left_sum + right_sum)

def find_maximum_subarray(arr, low, high):
    if high == low:
        return (low, high, arr[low])

    mid = (low + high) // 2

    left_low, left_high, left_sum = find_maximum_subarray(arr, low, mid)
    right_low, right_high, right_sum = find_maximum_subarray(arr, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return (left_low, left_high, left_sum)
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return (right_low, right_high, right_sum)
    else:
        return (cross_low, cross_high, cross_sum)

def simulate_stock_prices(days):
    return [random.randint(50, 120) for _ in range(days)]

def calculate_daily_changes(prices):
    return [prices[i] - prices[i-1] for i in range(1, len(prices))]

def test_and_print(arr):
    print("Input:", arr)
    low, high, max_sum = find_maximum_subarray(arr, 0, len(arr) - 1)
    max_subarray = arr[low:high+1]
    print("Maximum Subarray:", max_subarray)
    print("Sum:", max_sum)
    print()

# Test Cases
test_and_print([0, 1, -4, 3, -4])
test_and_print([0, -2, 4, 5, -6, 10, -4])
test_and_print([0, 13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])

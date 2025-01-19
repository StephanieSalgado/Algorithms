import random
from tabulate import tabulate

def generate_prices(num_days, min_price, max_price):
    return [random.randint(min_price, max_price) for _ in range(num_days)]

def calculate_price_changes(prices):
    return [prices[i] - prices[i - 1] for i in range(1, len(prices))]

def max_crossing(prices, low, mid, high):
    left_sum = float('-inf')
    right_sum = float('-inf')
    sum = 0
    max_left = mid

    for i in range(mid, low - 1, -1):
        sum += prices[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    sum = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        sum += prices[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum + right_sum

def max_subarray(prices, low, high):
    if high == low:
        return low, high, prices[low]
    
    mid = (low + high) // 2
    left = max_subarray(prices, low, mid)
    right = max_subarray(prices, mid + 1, high)
    cross = max_crossing(prices, low, mid, high)

    if cross[2] >= left[2] and cross[2] >= right[2]:
        return cross
    elif left[2] >= right[2]:
        return left
    else:
        return right

prices = generate_prices(100, 50, 120)

price_changes = calculate_price_changes(prices)

low, high, max_sum = max_subarray(price_changes, 0, len(price_changes) - 1)
max_subarray_prices = prices[low:high + 1]

# Prepare data for table
table_data = [["Day", "Price", "Change"]]
for i in range(len(prices)):
    if i > 0:
        change = prices[i] - prices[i - 1]
    else:
        change = 0
    table_data.append([i + 1, prices[i], change])

print(tabulate(table_data, headers="firstrow", tablefmt="grid"))
print()

print("Maximum Subarray:", max_subarray_prices)
print("Sum:", max_sum)

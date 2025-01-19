"""
Stephanie Salgado

April 09 2024

This program solves the knapsack problem using two different methods: knapsack_01 (dynamic programming) 
and fractional_knapsack (greedy strategy). The goal is to maximize the value of items while ensuring they 
fit within the knapsack's capacity. Test cases are provided to evaluate both algorithms with different item 
values, weights, and knapsack capacities, displaying the results for comparison.
"""
from tabulate import tabulate

    
    # Solve the 0-1 knapsack problem using dynamic programming
def knapsack_01(capacity, weights, values):

    num_items = len(values)
    # Initialize the dynamic programming table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(num_items + 1)]
    
    # Fill the table using bottom-up approach
    for i in range(1, num_items + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
    return dp[num_items][capacity]


    # Solve the fractional knapsack problem using a greedy algorithm
def fractional_knapsack(values, weights, capacity):
    # Create a list of tuples, each containing the value, weight, and value-to-weight ratio of an item
    items = sorted([(val, weight, val / weight) for val, weight in zip(values, weights)], key=lambda x: x[2], reverse=True)
    
    load = 0
    for item in items:
        value, weight, _ = item
        if weight <= capacity:
            load += value
            capacity -= weight
        else:
            # Take a fraction of the item
            fraction = capacity / weight
            load += value * fraction
            capacity = 0
            break
    return load

# Test cases
test_cases = [
    {"capacity": 100, "values": [20, 30, 40, 50, 60], "weights": [10, 20, 30, 40, 50]},
    {"capacity": 50, "values": [60, 100, 120], "weights": [10, 20, 30]},
    {"capacity": 15, "values": [10, 20, 30], "weights": [2, 5, 10]}
]

# Evaluate each test case
for idx, test in enumerate(test_cases, start=1):
    capacity = test["capacity"]
    values = test["values"]
    weights = test["weights"]
    
    # Calculate the maximum value using both algorithms
    max_value_knapsack_01 = knapsack_01(capacity, weights, values)
    max_value_fractional_knapsack = fractional_knapsack(values, weights, capacity)
    
    # Prepare table for results
    table = [
        ["", "", "", "Algorithm", "Maximum Value"],
        ["Capacity", "Values", "Weights", "0-1 Knapsack", max_value_knapsack_01],
        [capacity, values, weights, "Fractional Knapsack", max_value_fractional_knapsack]
    ]
    
    # Print the table
    print()
    print(tabulate(table, headers="firstrow", tablefmt="fancy_grid", numalign="center", stralign="center", showindex=False))
    print()


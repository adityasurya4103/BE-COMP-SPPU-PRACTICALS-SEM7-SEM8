def knapsack_dp(W, wt, val, n):
    """A Dynamic Programming based solution for 0-1 Knapsack problem.
    Returns the maximum value that can be stored in the knapsack."""
    # Create a 2D list to store the maximum value at each subproblem
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:

                # If wt[i - 1] <= w (i.e., the item's weight is less than or equal to the current capacity w), two options are evaluated:
                #     Include the item: Value = val[i - 1] + K[i - 1][w - wt[i - 1]] (current item value + optimal solution for     remaining capacity).
                #     Exclude the item: Value = K[i - 1][w] (optimal solution without current item).
                #     The maximum of these two values is chosen for K[i][w].
                
                
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:

                # If the item’s weight exceeds the capacity w, the item is excluded, and K[i][w] = K[i - 1][w]
                
                K[i][w] = K[i - 1][w]
    
    return K[n][W]


if __name__ == "__main__":
    # Taking user input for the number of items
    n = int(input("Enter the number of items: "))

    wt = []
    val = []

    # Taking user input for weights and values
    for i in range(n):
        weight = int(input(f"Enter weight of item {i + 1}: "))
        value = int(input(f"Enter value of item {i + 1}: "))
        wt.append(weight)
        val.append(value)

    # Taking user input for knapsack capacity
    W = int(input("Enter the capacity of the knapsack: "))

    # Function call to knapsack_dp
    max_profit = knapsack_dp(W, wt, val, n)
    print("Maximum possible profit =", max_profit)

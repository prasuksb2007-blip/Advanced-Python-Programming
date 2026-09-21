"""
Write a code for optimal selection of items to maximize value within a weight constraint using bottom-upand top-down approaches.
"""
# Top-Down Approach (Recursive with Memoization)
def knapsack_top_down_helper(values, weights, n, w, memo):
    # Base Case
    if n == 0 or w == 0:
        return 0
    
    # Return already computed subproblem
    if memo[n][w] != -1:
        return memo[n][w]
    
    # If weight of the nth item is greater than capacity W, it cannot be included
    if weights[n - 1] > w:
        memo[n][w] = knapsack_top_down_helper(values, weights, n - 1, w, memo)
        return memo[n][w]
    else:
        # Return the maximum of including or excluding the nth item
        include = values[n - 1] + knapsack_top_down_helper(values, weights, n - 1, w - weights[n - 1], memo)
        exclude = knapsack_top_down_helper(values, weights, n - 1, w, memo)
        memo[n][w] = max(include, exclude)
        return memo[n][w]

def knapsack_top_down(values, weights, W):
    n = len(values)
    # Initialize memoization table with -1
    memo = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]
    return knapsack_top_down_helper(values, weights, n, W, memo)


# Bottom-Up Approach (Tabulation)
def knapsack_bottom_up(values, weights, W):
    n = len(values)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
                
    return dp[n][W]


# Example usage and demonstration:
if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50
    
    print("Top-Down (Memoization) Output:", knapsack_top_down(values, weights, W))
    print("Bottom-Up (Tabulation) Output:", knapsack_bottom_up(values, weights, W))

"""
--> Output
Top-Down (Memoization) Output: 220
Bottom-Up (Tabulation) Output: 220
"""

"""
Write a program to find the longest common subsequence between two sequences.
"""
def LCS(X, Y):
    m = len(X)
    n = len(Y)

    # Step 1: Initialize the DP table with zeros
    lcs_table = [[0] * (n + 1) for _ in range(m + 1)]

    # Step 2: Build the DP table
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs_table[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])

    # Step 3: Backtrack to reconstruct the LCS string
    index = lcs_table[m][n]
    lcs_string = [""] * index
    
    i = m
    j = n
    
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_string[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs_string)


# --- Example Usage (As defined in Pseudocode) ---
if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"

    result = LCS(X, Y)

    print("=" * 45)
    print("      LONGEST COMMON SUBSEQUENCE (LCS)     ")
    print("=" * 45)
    print(f"Sequence 1 (X) : {X}")
    print(f"Sequence 2 (Y) : {Y}")
    print("-" * 45)
    print(f"Longest Common Subsequence: {result}")
    print(f"Length of LCS            : {len(result)}")
    print("=" * 45)

"""
--> Output
=============================================
      LONGEST COMMON SUBSEQUENCE (LCS)     
=============================================
Sequence 1 (X) : AGGTAB
Sequence 2 (Y) : GXTXAYB
---------------------------------------------
Longest Common Subsequence: GTAB
Length of LCS            : 4
=============================================
"""
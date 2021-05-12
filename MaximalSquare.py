'''
In this question we have to find the maximum sqaure in 1's and 2's matrix, we achieve this by having
seeing the adjacent three blocks to the current block, if they are one as well then we increase our 
side size
'''

def maximalSqaure(self,matrix):
    if not matrix:
        return 0

    m = len(matrix)
    n = len(matrix[0])

    dp = [[0]*(n+1) for _ in range(m+1)]

    maxSide = 0

    for r in range(m):
        for c in range(n):
            if matrix[r][c] == '1':
                dp[r+1][c+1] = min(dp[r][c], dp[r+1][c],dp[r][c+1]) + 1
                maxSide = max(maxSide,dp[r+1][c+1])

    return maxSide
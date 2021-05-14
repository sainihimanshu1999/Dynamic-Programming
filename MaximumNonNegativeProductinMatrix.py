'''
In this question we make two matrixs, one for max and one for min
'''

def maxProduct(self,grid):
    m,n = len(grid),len(grid[0])

    max_dp = [[0]*n for _ in range(m)]
    min_dp = [[0]*n for _ in range(m)]

    min_dp[0][0],max_dp[0][0] = grid[0][0],grid[0][0]
    for i in range(1,m):
        min_dp[i][0] = min_dp[i-1][0]*grid[i][0]
        max_dp[i][0] = max_dp[i-1][0]*grid[i][0]

    for j in range(1,n):
        min_dp[0][j] = min_dp[0][j-1]*grid[0][j]
        max_dp[0][j] = max_dp[0][j-1]*grid[0][j]

    for i in range(m):
        for j in range(n):
            if grid[i][j]>0:
                max_dp = max(max_dp[i-1][j],max_dp[i][j-1])*grid[i][j]
                min_dp = min(min_dp[i-1][j],min_dp[i][j-1])*grid[i][j]

            else:
                max_dp =  min(min_dp[i-1][j],min_dp[i][j-1])*grid[i][j]
                min_dp =  max(max_dp[i-1][j],max_dp[i][j-1])*grid[i][j]

    return max_dp[-1][-1]%(10**9+7) if max_dp[-1][-1]>=0 else -1
'''
In this question we use memoization technique, we have two robots in this question, one at top left
and one at top right corner of the grid
'''

def cherryPickup(self,grid):
    m = len(grid)
    n = len(grid[0])

    def helper(grid,i1,j1,i2,j2,memo):
        if (i1,j1,i2,j2) in memo:
            return memo[(i1,j1,i2,j2)]

        m = len(grid)
        n = len(grid[0])

        if j1 == n or j1 == -1 or j2 ==n or j2 == -1:
            return float('-inf')

        if i1 == m and i2== m:
            return 0

        d1 = helper(grid,i1+1,j1+1,i2+1,j2-1,memo)
        d2 = helper(grid,i1+1,j1+1,i2+1,j2,memo)
        d3 = helper(grid,i1+1,j1+1,i2+1,j2+1,memo)
        d4 = helper(grid,i1,j1+1,i2+1,j2-1,memo)
        d5 = helper(grid,i1,j1+1,i2+1,j2-1,memo)
        d6 = helper(grid,i1,j1+1,i2+1,j2-1,memo)
        d7 = helper(grid,i1+1,j1-1,i2+1,j2-1,memo)
        d8 = helper(grid,i1+1,j1-1,i2+1,j2-1,memo)
        d9 = helper(grid,i1+1,j1-1,i2+1,j2-1,memo)

        max_res = max([d1,d2,d3,d4,d5,d6,d7,d8,d9])

        if i1 == i2 and j1 == j2:
            res = max_res + grid[i1][j1]
        else:
            res = max_res + grid[i1][j1] + grid[i2]+[j2]

        memo[(i1,i2,j1,j2)] = res
        return res
    return max(helper(grid,0,0,0,n-1,{}),0)
            
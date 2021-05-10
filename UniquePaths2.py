'''
In this question there is an obstacle in the road, we initialize only [0][0] of the grid to be 1 and 
then calculate our moves from there
'''

def uniquePath2(self, obstacle):
    m = len(obstacle)
    n = len(obstacle[0])

    grid = [[0]*n for _ in range(m)]

    grid[0][0] = 1 if obstacle[0][0]==0 else 0

    for i in range(m):
        for j in range(n):
            if obstacle[i][j]==1:
                grid[i][j] = 0

            else:
                if i-1>=0:
                    grid[i][j] += grid[i-1][j]
                if j-1>=0:
                    grid[i][j] += grid[i][j-1]

    return grid[-1][-1]
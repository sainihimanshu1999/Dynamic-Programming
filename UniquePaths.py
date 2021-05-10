'''
In general path sum a grid is made
'''

def UniquePath(self,m,n):
    mat = [[1]*n for i in range(m)]

    for i in range(1,m):
        for j in range(1,n):
            mat[i][j] = mat[i-1][j] +  mat[i][j-1]

    return mat[-1][-1]

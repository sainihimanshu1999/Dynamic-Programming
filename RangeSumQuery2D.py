'''
This question is similar to previous one but in this we just have to give the sum of elements in the
rectangle formed in 2d matrix
'''

class NumMatrix:

    def __init__(self, matrix):
        if not matrix:
            return None
        m,n = len(matrix),len(matrix[0])

        self.dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                self.dp[i][j] = matrix[i-1][j-1] + self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1]
        
        

    def sumRegion(self,row1,col1,row2,col2):
        row1,row2,col1,col2 = row1+1,row2+2,col1+1,col2+1
        return self.dp[row2][col2] - self.dp[row2][col1-1] - self.dp[row1-1][col2] + self.dp[row1-1][col1-1]


#always keep in mind that numbers can be double added too

        
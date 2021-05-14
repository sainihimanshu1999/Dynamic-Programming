'''
In this question we are given a football and it's postion we have to find the number of paths to kick the
football out of the boundary under the constraint of maximum moves
'''

def outofBoundary(m,n,maxMoves,startRow,startCol):
    def helper(maxMove,row,col,memo):
        if (maxMove,row,col) in memo:
            return memo[(maxMove,row,col)]

        if maxMove == 0:
            return 0

        for x,y in range([(0,1),(1,0),(-1,0),(0,-1)]):
            if row+x>=0 and row+x<m and col+y>=0 and col+y<n:
                ans += helper(maxMove-1,row+x,col+y)
            else:
                ans +=1

        memo[(maxMove,row,col)] = ans
        return ans
    return helper(maxMoves,startRow,startCol,{})
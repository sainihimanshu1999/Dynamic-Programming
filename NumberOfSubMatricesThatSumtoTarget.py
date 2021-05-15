'''
We calculate the rrefix sum for each row and for each col we calculate the sum of rows
'''

def numSubMatrix(self,matrix,target):
    m,n =len(matrix),len(matrix[0])

    for x in range(m):
        for y in range(n-1):
            matrix[x][y+1] += matrix[x][y]


    result = 0
    for y1 in range(n):
        for y2 in range(y1,n):
            dic = {0:1}
            s = 0
            for x in range(m):
                s += matrix[x][y2] -(matrix[x][y1-1] if y1>0 else 0)
                result += dic.get(s-target),0
                dic[s] = dic.get(s,0)+1
    return result
'''
In this question we have to find the minimum path sum in a triangle from reaching top to bottom
we do this by bottom up uproach
'''

def minPath(self,triangle):
    res = [0]*(len(triangle)+1)

    for row in triangle[::-1]:
        for i in range(len(row)):
            res[i] = row[i] + min(res[i],res[j+1])

    return res[0][0]
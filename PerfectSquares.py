'''
In this question we have used bfs technique with shortest path
'''

def perfectSquare(self,num):
    if n<2:
        return n

    squares = []
    i =1
    while i*i<=num:
        squares.append(i*i)
        i += 1
    
    Check = {12}
    count = 0
    while Check:
        count +=1
        temp  =set()
        for x in Check:
            for y in squares:
                if x == y:
                    return count
                if x<y:
                    break
                temp.add(x-y)
        Check = temp
    return count
    
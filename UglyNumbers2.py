'''
In this question we have to find nth ugly number, the number whic have prime factors like 2,3 and 5.
we keep three pointers to get indivdual multiple and whatever is minimum in this we add that to ugly array
'''

def ugly(self,n):
    i2,i3,i5 = 0,0,0
    ugly = [1]
    while n>1:
        u2,u3,u5 = 2*ugly[i2], 3*ugly[i3], 5*ugly[i5]
        umin = min(u2,u3,u5)

        if umin == u2:
            i2 +=1

        if umin == u3:
            i3+=1

        if umin == u5:
            i5+=1
        ugly.append(umin)
        n-=1
    return ugly[-1]

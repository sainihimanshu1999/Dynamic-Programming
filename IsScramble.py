'''
In scramble list we have to divide and join reversingly and keep doing this until the len of string is one
'''

def isScramle(self,s1,s2):
    def f(s1,s2,memo):
        if (s1,s2) in memo:
            return memo[(s1,s2)]

        if len(s1)!=len(s2) or sorted(s1)!=sorted(s2):
            memo[(s1,s2)] = False
            return False

        if s1 == s2:
            memo[(s1,s2)] = True
            return True

        for i in range(1,len(s1)):
            if (f(s1[i:],s2[i:],memo) and f(s1[:i],s2[:i],memo) or \
            f(s1[:i],s2[-i:],memo)and f(s1[i:],s2[:-i],memo)):
                return True
        memo[(s1,s2)] = False
        return memo[(s1,s2)]

    return f(s1,s2,{})
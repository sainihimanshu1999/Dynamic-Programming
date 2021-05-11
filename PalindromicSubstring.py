'''
checking by slicing one bye one slicing
'''

def palindrome(self,s):
    n = len(s)
    result = []

    def dfs(ret,m):
        if m ==n:
            result.append(ret)
            return

        for i in range(m,n):
            temp = s[m:i+1]
            if temp == temp[::-1]:
                dfs(ret+[temp],m+1)
    dfs([],0)
    return result

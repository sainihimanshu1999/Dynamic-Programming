'''
Distinct Subsequence
'''

def distinctSubsequence(self,s,t):
    l1 = len(s)+1
    l2 = len(t)+1

    cur = [0]*l2
    cur[0] = 1

    for i in range(1,l1):
        p = cur[:]
        for j in range(1,l2):
            cur[j] = p[j] + p[j-1]*(s[i-1]==t[j-1])

    return cur[-1]
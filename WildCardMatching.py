'''
difference between regualr matching and wildcard matching is '*' in regex only copies precedding element
and '*' in copy any number of element even empty string
'''

def wildcard(self,s,p):
    n = len(s)
    m = len(p)

    dp [[False]*(m+1) for _ in range(n+1)]

    dp[0][0] = True


    for i in range(1,m+1):
        if p[i-1]!='*':
            break
        dp[0][m] = True


    for i in range(1,n+1):
        for j in range(1,m+1):
            if p[j-1] == s[i-1] or p[j-1] == '?':
                dp[i][j] = dp[i-1][j-1]

            elif p[j-1] == '*':
                dp[i][j] = dp[i-1][j-1] or dp[i-1][j] or dp[i][j-1]

    return dp[-1][-1]
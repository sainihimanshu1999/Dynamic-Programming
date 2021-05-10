def isMatch(self,s,p):
    n = len(s)
    m = len(p)

    dp = [[False]*(m+1) for _ in range(n+1)]

    dp[0][0] = True

    for i in range(1,m+1):
        if i>1 and p[i-2] == '*':
            dp[0][i] = dp[0][i-2]


    for i in range(1,n+1):
        for j in range(1,m+1):
            if p[j-1] == '.' or p[j-1]==s[i-1]:
                dp[i][j] = dp[i-1][j-1]

            elif j>2 and p[i-2]=="*":
                if p[j-2] == s[i-1] or p[j-2] =='.':
                    dp[i][j] = dp[i][j-2] or dp[i-1][j]

                else:
                    dp[i][j] = dp[i][j-2]

    return dp[n][m]
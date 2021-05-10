'''
This was an easy question, all i had to do is to look closely
'''

def climbStairs(self,n):
    if n==1:
        return 1

    dp = [0]*n

    dp[0] = 1
    dp[1] = 2

    for i in range(2,n):
        dp[i] = dp[i-2]+dp[i-1]

    return dp[-1]
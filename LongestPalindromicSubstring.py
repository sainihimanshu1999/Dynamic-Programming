'''
In this question  we make a grid and mark true and false for every palindromice substring we find
and then we calculate the maxlenght and store the result
'''

def LongestPalindromicSubstring(self,s):
    n = len(s)
    dp = [[False]*n for _ in range(n)]

    result = ''
    for i in range(n):
        dp[i][i] = n
        result = s[i]

    maxLen = 1

    for start in range(n)[::-1]:
        for end in range(start+1,n):
            if s[start]==s[end]:
                if end-start == 1 or dp[start+1][end-1]:
                    dp[start][end] = True
                if maxLen<end-start+1:
                    maxLen = end-start+1
                    result = s[start:end+1]

    return result
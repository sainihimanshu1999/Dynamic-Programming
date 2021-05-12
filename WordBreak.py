'''
Simple Recursion
'''
def wordBreak(self,s,wordDict):
    if not s:
        return True

    for word in wordDict:
        if s[:len(word)] == word:
            if len(s) == len(word):
                return True

            else:
                suffix = s[len(word):]
                if (self.wordBreak(suffix,wordDict)):
                    return True

    return False



'''
With Memoization
'''

def wordBreakM(self,s,wordDict):
    def dfs(self,s,wordDict,memo):
        if s in memo:
            return memo[s]

        for word in wordDict:
            if s[:len(word)] = word:
                if len(s) == len(word):
                    memo[s] = True
                    return True

                else:
                    suffix = s[len(word):]
                    if dfs(suffix,wordDict,memo):
                        memo[s] = True
                        return True
        memo[s] = False
        return memo[s]

    return dfs(s,wordDict,{})
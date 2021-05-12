'''
This question is solved just by a simple recursion
'''

def wordBreak(self,s,wordDict):
    if not s:
        return [[]]

    result = []
    for word in wordDict:
        if s[:len(word)] == word:
            if len(s) == len(word):
                result.append(word)

            else:
                suffix = s[len(word):]
                temp = self.wordBreak(suffix,wordDict)
                for t in temp:
                    result.append(word+' '+t)

    return result

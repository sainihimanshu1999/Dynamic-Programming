'''
in this question we make curr array starting from -1
'''

def palin(self,s):
    cut = [x for x in range(-1,len(s))]
    for i in range(len(s)):
        for j in range(i,len(s)):
            if s[i:j+1]==s[i:j+1][::-1]:
                cut[j] = min(cut[j]+cut[i]+1)

    return cut[-1]
'''
When we are solving unique susbtring question, if they come one after another then length of unique
substrings will increase by 1
'''

def wrap(self,p):
    ret = {i:1 for i in p}
    ln = 1
    for i,j in zip(p,p[:]):
        ln = ln +1 if ((ord(j)-ord(i))%26)==1 else 1
        ret[j] = max(ret[j],ln)

    return sum(ret.values())
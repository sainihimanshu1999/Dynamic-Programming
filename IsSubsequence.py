'''
In this solution we are using two pointer approach, 
'''

def subSequence(self,s,t):
    pos_s,pos_t = 0,0

    while pos_s<len(s) and pos_t<len(t):
        pos_s,pos_t = pos_s + (s[pos_s]==t[pos_t]), pos_t + 1

    return pos_s == len(s)
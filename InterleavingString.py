'''
in interleaving string s1+s2 = s3, where interleaving s1+t1+s2+t2+s3+t3
'''
def interLeaving(self,s1,s2,s3):
    def f(s1,s2,s3,memo):
        if (s1,s2,s3) in memo:
            return memo[(s1,s2,s3)]

        if len(s1)+len(s2) != len(s3):
            memo[(s1,s2,s3)] = False
            return False
        if not s1 and not s2 and not s3:
            memo[(s1,s2,s3)] = True
            return True
        ans = (len(s1)>0 and len(s3)>0 and s1[0] == s3[0] and f(s1[1:],s2,memo)) or \
            len(s2)>0 and len(s3)>0 and s2[0] == s3[0] and f(s1,s2[1:],memo)

        memo[(s1,s2,s3)] = ans

        return memo[(s1,s2,s3)]

    return f(s1,s2,s3,{})

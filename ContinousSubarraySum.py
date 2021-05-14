'''
Continous sub array sum, in this question, if sum(nums[i:j])%k==0 then sum(nums[:i])%k == sum(nums[:j])%k
'''

def subarraysum(self,nums,k):
    dic = {0:-1}
    summ = 0

    for i,n in enumerate(nums):
        if k!=0:
            summ = (summ+n)%k
        else:
            summ += n

        if summ not in dic:
            dic[summ] = i
        else:
            if i-dic[summ]>=2:
                return True
    return False
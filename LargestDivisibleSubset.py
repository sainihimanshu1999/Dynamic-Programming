'''
This is a medium level question, but a little bit tricky
'''

def largestDivisibleSubset(self,nums):
    if len(nums) == 0:
        return []

    nums.sort()
    ret = [[num] for num in nums]

    for i in range(len(nums)):
        for j in range(i):
            if nums[i]%nums[j] == 0 and len(ret[i])<len(ret[j])+1:
                ret[i] = ret[j] + [nums[i]]

    return max(ret,key=len)
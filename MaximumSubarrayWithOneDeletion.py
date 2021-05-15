'''
We use the concept of maximum subarray sum in this with just a little twist
'''

def maxSubarraywithDeletion(self,nums):
    n = len(nums)
    max_ending0 = [nums[0]]*n
    max_ending1 = [nums[0]]*n

    for i in range(1,n):
        max_ending0[i] = max(max_ending0[i-1]+nums[i],nums[i])
        max_ending1[i] = max(max_ending1[i-1]+nums[i],nums[i])

        if i>=2:
            max_ending1[i] = max(max_ending1[i],max_ending0[i-2]+nums[i])

    return max(max_ending1)

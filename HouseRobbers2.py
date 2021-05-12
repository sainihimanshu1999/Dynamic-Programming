'''
This question is just an alteration of house robber 1, with starting and ending houses being the neighbour
of each other, so we can loot them either
'''

def robber(self,nums):
    if not nums:
        return 0
    elif len(nums) ==1:
        return nums[0]
    else:
        x = nums[:]
        nums = nums[1:]
        dp1,dp2 = 0,0
        for num in nums:
            dp1,dp2 = dp2,max(dp1+num,dp2)

        dp3,dp4 = 0,0
        x = x[:-1]
        for i in x:
            dp3,dp4 = dp4, max(dp3+i,dp4)

        return max(dp2,dp4)
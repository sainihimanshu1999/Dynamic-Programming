'''
We take minimum of rightmax and left max array and subtract the current height from it
'''

def trapWater(self,nums):
    n = len(nums)
    leftMax = [0]*n
    rightMax = [0]*n

    water = [0]*n

    left=0
    right = 0


    for i in range(n):
        left = max(left,nums[i])
        leftMax[i] = left


    for i in range(n)[::-1]:
        right = max(right, nums[i])
        rightMax[i] = right

    for i in range(n):
        water[i] = min(leftMax[i],rightMax[i]) - nums[i]

    return sum(water)
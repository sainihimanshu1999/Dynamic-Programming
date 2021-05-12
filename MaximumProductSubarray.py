'''
here we have to find maximum prodcut CONTIGOUS subarray
'''

def maxProd(self,nums):
    x = nums[::-1]

    for i in range(len(nums)):
        nums[i]  *= nums[i] or 1
        x[i] *= x[i] or 1

    return max(nums+x)
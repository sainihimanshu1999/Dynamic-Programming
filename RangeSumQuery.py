'''
In this question we have given queries, to give the sum in the range(i,j) to make the solution time
complexity constant, we make our primary array to have sum of elements until last
'''

class NumArray:

    def __init__(self, nums):
        self.arr = []
        sum_till = 0
        for num in nums:
            sum_till += num
            self.arr.append(sum_till)        
        

    def sumRange(self, left, right):
        if left>0 and right>0:
            return self.arr[right] - self.arr[left-1]

        else:
            return self.arr[left or right]
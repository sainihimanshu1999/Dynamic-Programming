'''
Bitwise or compares each bit of the number and return 1 when one of the bit is one of two numbers.
In this question we are making at list of set of the existing numbers and, then calculating the or
of last number with previous number and then saving the value in a set
'''

def bitWiseOr(self,nums):
    table = [set(nums[i]) for i in range(len(nums))]
    for i in range(1,len(nums)):
        for pre in table[i-1]:
            table[i].add(nums[i]|pre)


    return len(set.union(*table)) if len(nums)>0 else 0



'''
In this question we have made an array, and then maintain the position and check every number of array
that we have created is equal or less than the number of array we are on the input
'''

def LIS(self,nums):
    sub = []

    for num in nums:
        pos = 0
        len_sub = len(sub)

        while(pos<=len_sub):
            if pos == len_sub:
                sub.append(num)
                break
            elif num<=sub[pos]:
                sub[pos] = num
                break
            else:
                pos +=1
        return len(sub)


'''
Another method of solving this question
'''

def LIS2(self,nums):
    if not nums: return 0

    length = [1]*(len(nums))

    for i in range(len(nums)):
        for j in range(i):
            if nums[i]>nums[j]:
                if length[i]==length[j]:
                    length[i] = length[j]+1
    
    return max(length)
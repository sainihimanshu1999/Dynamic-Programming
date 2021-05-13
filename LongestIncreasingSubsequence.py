'''
In this question we have made an array, and then maintain the position and check every number of array
that we have created is equal or less than the number of array we are on the input
'''

def LIS(self,nums):
    sub = []

    for num in nums:
        pos = 0
        len_sub = len(sub)

        for num in nums:
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
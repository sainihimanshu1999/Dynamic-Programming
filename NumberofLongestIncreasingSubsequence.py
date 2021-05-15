'''
This question is similar to longest increasing subsquence, we have to use the same approach but just have 
to maintain an count array to keep the count of loongest increasing subseqeunces
'''

def NLIS(self,nums):
    if not nums:return 0
    n = len(nums)
    length  = [1]*n
    count = [1]*n

    for i in range(n):
        for j in range(i):
            if nums[i]>nums[j]:
                if length[i]==length[j]:
                    length[i] = length[j]+1
                    count[i] = count[j]
                elif length[i] == length[j]+1:
                    count[i] = count[j]+1

    maxLen = max(length)
    return sum([count[i] for i in range(n) if length[i] == maxLen])
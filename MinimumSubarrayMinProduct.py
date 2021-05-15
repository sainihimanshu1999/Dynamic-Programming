'''
In this question we use monotonic stack, monotonic stack is a useful data structure which helps in knowing
the boundary of things, used in many questions like maximum area in histogram etc
'''

def minProd(self,nums):
    stack = [(-1,0)]
    running_sum = 0
    max_sum = 0

    nums.append(0)

    for v in nums:
        while stack[-1][0] >= v:
            min_val,i = stack.pop()
            max_sum = max(max_sum, min_val*(running_sum-stack[-1][1]))
        
        running_sum += v
        stack.append((v,running_sum))
    return max_sum
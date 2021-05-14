'''
When we have to find the maximum sum subarray, we generally use kadane's algorithm. In kadane's algorithm
we have two variables, max_ending and max_sum_sofar. we move max_ending one by one and update max_sum if
max_ending is greater than before
'''

def maxSubarray(self,arr,k):
    def kadane(self,a):
        max_sum_sofar, max_ending= 0,0
        for i in range(len(a)):
            max_ending = max_ending + a[i]

            if max_ending>0:
                max_sum_sofar = max(max_sum_sofar,max_ending)

            elif max_ending<0:
                max_ending = 0

        return max_sum_sofar

    if not arr:
        return 0

    s = sum(arr)
    if k == 1:
        return max(0,kadane(arr))%(10**9+7)
    else:
        return max(0,(k-2)*max(s,0)+kadane(arr+arr))%(10**9+7)
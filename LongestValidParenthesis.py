'''
In this question we have to count the length f longest valid paranthesis
'''

def validParan(self,s):
    stack = [0]
    count = 0

    for i in s:
        if i == '(':
            stack.append(0)
        else:
            if len(stack)>1:
                val = stack.pop()
                stack[-1] += val +2

                count = max(count,stack[-1])

            else:
                stack = [0]

    return count
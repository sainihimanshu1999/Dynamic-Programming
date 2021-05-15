'''
In this question we have to find the sum of total tree and then subtract the sum of subtrees and check the
max product
'''

def maxProd(self,root):
    arr = []
    def subtree(node):
        if not node: return 0
        ans = node.val + subtree(node.left) +  subtree(node.right)
        arr.append(ans)
        return ans

    total = subtree(root)
    return max((x*(total-x)) for x in arr)
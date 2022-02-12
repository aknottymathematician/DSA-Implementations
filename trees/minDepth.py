# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# def minDepth(root) -> int:
#     if not root:
#         return 0
    
#     if not root.left and not root.right:
#         return 1

#     if not root.left:
#         return 1 + minDepth(root.right)
#     elif not root.left:
#         return 1 + minDepth(root.left)
    
#     else:
#         return min(minDepth(root.left), minDepth(root.right))+1

# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root) -> int:
        
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1

        if not root.left:
            return 1 + self.minDepth(root.right)
        elif not root.left:
            return 1 + self.minDepth(root.left)
        
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right))+1

# Driver function to test the above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)

sol = Solution()

print(sol.minDepth(root))
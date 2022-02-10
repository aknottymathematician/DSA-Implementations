class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

'''
Approach I
Time Complexity - O(N^2){In case of full binary tree}
This approach can be optimized by calculating height in the same recursion rather than calling height function separately.
Optimization reduces time complexity to O(N)
'''
def height(root):
	if not root:
		return 0
	return max(height(root.left), height(root.right)+1)

def isBalanced( root):

	if not root:
		return False

	lh = height(root.left)
	rh = height(root.right)

	if abs(lh-rh)<=1 and isBalanced(root.left) and isBalanced(root.right):
		return True
	return False

# Driver function to test the above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
if isBalanced(root):
    print("Tree is balanced")
else:
    print("Tree is not balanced")
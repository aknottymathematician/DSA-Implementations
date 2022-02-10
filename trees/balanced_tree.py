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

# # function to find height of binary tree
# def height(root):
# 	if not root:
# 		return 0
# 	return max(height(root.left), height(root.right))+1

# # function to check if tree is height-balanced or not
# def isBalanced( root):

# 	#Base condition
# 	if not root:
# 		return True

# 	#Calculate height for left and right subtree
# 	lh = height(root.left)
# 	rh = height(root.right)

# 	#Allowed height differences (lh-rh) are 1,-1,0
# 	if abs(lh-rh)<=1 and isBalanced(root.left) and isBalanced(root.right):
# 		return True
# 	return False


'''
Approach II
Time Complexity - O(N)
Auxillary Space - O(N)
'''
class HeightVar:
	def __init__(self):
		self.height = 0

def height(root):
	if not root:
		return 0

	return max(height(root.left), height(root.right))+1

def isBalanced(root):

	if not root:
		return True

	lh = HeightVar()
	rh = HeightVar()

	lh.height = height(root.left)
	rh.height = height(root.right)

	lb = isBalanced(root.left)
	rb = isBalanced(root.right)

	if abs(lh.height-rh.height) <= 1:
		return lb and rb

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
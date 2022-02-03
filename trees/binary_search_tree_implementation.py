#Node class defines the structure of the node
class BinarySearchTreeNode:
	#Initializing attributes of the node
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def add_child(self, data):
		if data == self.data: # making sure value doesn't exist already
			return
		if data < self.data:
			# add data to left subtree
			if self.left: # self.left is a subtree
				self.left.add_child(data)
			else: # self.left is a leaf node
				self.left = BinarySearchTreeNode(data)
		else:
			# add data to right subtree
			if self.right: # self.right is a subtree
				self.right.add_child(data)
			else: # self.right is a leaf node
				self.right = BinarySearchTreeNode(data)


	def inorder_traversal(self):
		elements = []
		# Left -> Root -> Right
		if self.left:
			elements += self.left.inorder_traversal()

		elements.append(self.data)

		if self.right:
			elements += self.right.inorder_traversal()

		return elements

	
	def preorder_traversal(self):
		elements = []
		# Root -> Left -> Right 
		elements.append(self.data)

		if self.left:
			elements += self.left.preorder_traversal()

		if self.right:
			elements += self.right.preorder_traversal()

		return elements


	def postorder_traversal(self):
		elements = []
		# Left -> Right -> Root
		if self.left:
			elements += self.left.postorder_traversal()

		if self.right:
			elements += self.right.postorder_traversal()

		elements.append(self.data)

		return elements


	def search(self, value):
		if self.data == value:
			return True

		if value < self.data:
			# value maybe in left subtree
			if self.left:
				return self.left.search(value)
			else: # leaf node
				return False

		if value > self.data:
			#value maybe in right subtree
			if self.right:
				return self.right.search(value)
			else: #leaf node
				return False


	def find_max(self):
		if self.right is None: # Right most leaf node
			return self.data
		return self.right.find_max()

	def find_min(self):
		if self.left is None: # Left most leaf node
			return self.data
		return self.left.find_min()


	def calculate_sum(self):
		left_sum = self.left.calculate_sum() if self.left else 0
		right_sum = self.right.calculate_sum() if self.right else 0

		return self.data + left_sum + right_sum


	def delete(self, value):
		if self.data is None:
			print("tree is empty")
			return
		if value < self.data:
			if self.left:
				self.left = self.left.delete(value)
			else:
				return None
		elif value > self.data:
			if self.right:
				self.right = self.right.delete(value)
		else:
			if self.left is None and self.right is None:
				return None
			if self.left is None:
				temp = self.right
				self = None
				return temp

			if self.right is None:
				temp = self.left
				self = None
				return temp

			node = self.right
			while node.left:
				node = node.left
			self.data = node.data
			self.right = self.right.delete(node.data)
		return self	
			
			# min_value = self.right.find_min()
			# self.data = min_value
			# self.right = self.right.delete(min_value)

		# return self



# Helper Method
def build_tree(elements):
	root = BinarySearchTreeNode(elements[0])

	for i in range(1, len(elements)):
		root.add_child(elements[i])

	return root

if __name__ == '__main__':
	numbers = [17,4,12,3,14,19,3,2,34]
	numbers_tree = build_tree(numbers)
	print(numbers_tree.delete(12))
	print(numbers_tree.inorder_traversal())
	# print(numbers_tree.preorder_traversal())
	# print(numbers_tree.postorder_traversal())
	# print(numbers_tree.find_max())
	# print(numbers_tree.find_min())
	# print(numbers_tree.calculate_sum())
	
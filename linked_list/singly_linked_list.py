class Node:
	"""
	An object for storing a single node of a linked list
	Models two attributes - data and the link to the next node in the list
	"""
	def __init__(self, data=None, next = None):
		self.data = data
		self.next = next

	def __repr__(self):
		return "<Node data: %s>" %self.data


class LinkedList:
	"""
	Singly Linked List
	"""

	def __init__(self):
		self.head = None

	def insertStart(self, data):
		"""
		Insert element at the start of the linked list
		"""

		node = Node(data, self.head)
		self.head=node

	def insertEnd(self, data):
		"""
		Insert element at the end of the linked list
		"""

		if self.head is None:
			self.head = Node(data, None)
			return
		itr = self.head
		while itr.next:
			itr = itr.next
		itr.next = Node(data, None)


	def insertValues(self, data_list):
		"""
		Insert either at the start of the end of the linked list 
		"""

		self.head = None
		for data in data_list:
			self.insertStart(data)

	def getLength(self):
		"""
		Get the length of the linked list
		"""

		count = 0
		itr = self.head
		while itr:
			count +=1
			itr = itr.next
		return count

	def removeNode(self, index):
		"""
		Remove the element at the given index
		"""

		if index < 0 or index>self.getLength():
			raise Exception("Invalid Index")

		elif index == 0:
			self.head = self.head.next

		count = 0
		itr = self.head
		while itr:
			if count == index-1:
				itr.next = itr.next.next
				break

			itr = itr.next
			count+=1

	def insertNode(self, index, value):
		"""
		Given an index insert a value at that index in the linked list
		"""

		if index < 0 or index>self.getLength():
			raise Exception("Invalid Index")
		elif index == 0:
			self.insertStart(value)
			return
		count = 0
		itr = self.head
		while itr:
			if count == index-1:
				node = Node(value, itr.next)
				itr.next = node
				break

			itr = itr.next
			count +=1

	def printNode(self):
		if self.head is None:
			print("Linked List is empty")
			return

		itr = self.head
		llstr = ''

		while itr:
			llstr += str(itr.data)+"-->"
			itr = itr.next

		print(llstr)


	def insertAftervalue(self, data_after, value):
		# Search for the first occurence of the data_after value in linked list
		# Now insert value after data_after node
		if self.head is None:
			print("Linked List is Empty")
			return
		
		if self.head.data == data_after:
			self.head.next = Node(value, self.head.next)
			return


		itr = self.head
		while itr:
			print(itr)
			if itr.data == data_after:
				itr.next = Node(value, itr.next)
				break
			itr = itr.next
			

	def removeByvalue(self, data):
		# Remove first node that contains data
		if self.head is None:
			print("Linked List is Empty")
			return
		if self.head == data:
			self.head = self.head.next
			return

		itr = self.head
		count = 0
		while itr:
			# if itr.data == data:
			# 	print(count)
			# 	self.removeNode(count)
			# 	break
			if itr.next.data == data:
				itr.next = itr.next.next
				break
			itr = itr.next
		



if __name__ == "__main__":
	ll = LinkedList()
	ll.insertValues(["mango","apple","cheary","banana"])
	ll.printNode()
	ll.insertNode(1, "figs")
	ll.insertNode(2, "jackfruit")
	ll.printNode()
	ll.insertAftervalue("jackfruit", "peach")
	ll.printNode()
	ll.removeByvalue("cheary")
	ll.printNode()
	# print("Length of Linked List", ll.getLength())

		
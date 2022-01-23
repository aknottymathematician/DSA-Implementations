class HashTable:
	def __init__(self):
		self.SIZE = 10
		self.arr = [[] for i in range(self.SIZE)]

	def get_hash(self, key):
		hash = 0
		for char in key:
			hash += ord(char)
		return hash % self.SIZE

	'''
	In the original implementation in case of collision, the value was overwritten.
	To overcome that we are using chaining method
	'''
	def __setitem__(self, key, value):
		h = self.get_hash(key)
		found = False
		#first check if the key already exists
		for idx, element in enumerate(self.arr):
			if len(element)==2 and element[0]==key:
				#we cannot write element[1]=value since element is a tuple and tuples are immutable
				self.arr[h][idx] = (key, val)
				found = True
				break
		#if the key does not exist
		if not found:
			self.arr[h].append((key, value))

	def __getitem__(self, key):
		h = self.get_hash(key)
		for element in self.arr[h]:
			if element[0]==key:
				return element[1]


	def __delitem__(self, key):
		h = self.get_hash(key)
		for idx, element in enumerate(self.arr[h]):
			if element[0]==key:
				del self.arr[h][idx]

t = HashTable()
t["march 6"] = 110
t["march 8"] = 87
t["march 13"] = 4
t["march 17"] = 343

print(t["march 17"])
print(t.arr)
del t["march 17"]
print(t.arr)
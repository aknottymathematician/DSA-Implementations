from collections import deque

'''
You can use stack directly from the deque class, with in-built pop and append functions.
But just to understand the stack prototype, I am implement the stack class 
'''

class Stack:
	def __init__(self):
		self.container = deque()

	def push(self, value):
		self.container.append(value)

	def pop(self):
		return self.container.pop()

	def peek(self):
		return self.container[-1]

	def is_empty(self):
		return len(self.container) == 0

	def size(self):
		return len(self.container)

s = Stack()
s.push(6)

print(s.is_empty())
'''
Write a function in python that can reverse a string using stack data structure.

reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

'''

from collections import deque

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
		return len(self.container)==0

	def size(self):
		return len(self.container)

	def reverse_string(self, string):
		for char in string:
			self.push(char)
		rev_str = ''
		while self.size()!= 0:
			rev_str+=self.pop()
		return rev_str

s = Stack()
print(s.reverse_string("We will conquere COVID-19"))
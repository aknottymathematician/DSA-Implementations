import random

#Initializing an array
data = [random.random() for x in range(10000)]

#Accessing a memory in the array
print("Accessing the memory",data[1000])

#Overwriting an element in 8000th place
print("\nChecking position before overwriting",data[8000])
data[8000] = 104355
print("\nChecking position after overwriting",data[8000])

#Traversing thorugh an array
for i in data:
	if i > 100000:
		print("\nTraverse the array","True")


#Insert in an array
print("\nCheck position before inserting",data[500])
data.insert(500, 1600)
print("\nChecking new entries after inserting",data[500], data[501])

#Pop an element
print("\nElements before pop",data[899], data[900])
data.pop(899)
print("\nElement after pop",data[899])

#Remove an element
print("\nElements before removing",data[8000], data[8001])
data.remove(104355)
print("\nElements after removing",data[8000])

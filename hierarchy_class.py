from queue_raw import *
from DDL_GfG import DoublyLinkedList as queue


n = True
hierachy = queue()
hierachy.push("Employee")
hierachy.push("Manager ")
hierachy.push("Senior Manager")
hierachy.push("Director ") 
hierachy.push("Vice President")
hierachy.push("President")


while n:
	print("request type: from")
	print("0- Employee \n1- Manager \n2-Senior Manager \n3- Director \n4- Vice President \n5- President ")
	status = int(input("From 0 to 5:      "))
	type(status)
	print("\n\nWhat is your request")
	request = input("in:      ")

	# End the Goddon loop 
	n = False 
	

print (hierachy.head.data)

#This is the method to iterate through the Created Queue
node = hierachy.head
while(node is not None): 
		
		print ((node.data))
		last = node
		node = node.next
# print(hierachy)






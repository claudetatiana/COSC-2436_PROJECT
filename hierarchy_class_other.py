from queue_raw import *
from DDL_GfG import DoublyLinkedList as queue


n = True
hierachy = queue()
hierachy.push(0)
hierachy.push(1)
hierachy.push(2)
hierachy.push(5) 
hierachy.push(4)
hierachy.push(5)


print("request type: from")
print("0- Employee \n1- Manager \n2-Senior Manager \n3- Director \n4- Vice President \n5- President ")
status = int(input("From 0 to 5:      "))

print("\n\n Requests are orders as followed: \n0- $0 to $1000 \n1- $1000 tp $2000 \n2-$2000 to $5000 \n3- $5000 to $10K \n4- Above $10K \n5- President ")
print("Vacation request must be approved by the 2 level above the current requestee")
print("\n\nWhat is your request")
request = int(input("in:      "))
print("0- $0 to $1000 \n1- $1000 tp $2000 \n2-$2000 to $5000 \n3- $5000 to $10K \n4- Above $10K \n5- President ")


''' Rules of approval:
		Price oriented item: The level of approval is infered in the ordering
		of the request levels
		Vacations: Must be approves by the 1 level above

		A Kind of Pseudocode will:
		Approval = current approval level 
''
	


print (hierachy.head.data)

#This is the method to iterate through the Created Queue
node = hierachy.head
while(node is not None): 
		
		print ((node.data))
		last = node
		node = node.next
# print(hierachy)






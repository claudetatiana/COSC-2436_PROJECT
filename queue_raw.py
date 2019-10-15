class DNode(object):
    def __init__(self, data, next = None,prev=None):
        self.data = data
        self.next = next
        self.prev=prev
    def getItem(self):       
        if self.next==None:
            print (self.item)
        return 
        getItem(self.next)
        print (self.item)


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self,item):
        if self.head == None: 
            self.head = item
            self.tail = item
        else:
            self.tail.next = item
            item.previous = self.tail
            self.tail = item
    def remove(self):
        item = self.head 
        print('Removing ...',item.data)
        self.head = item.next
        return item
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    def getItem(self,item):
        node=self.head
        while node.next!=None:
            if node.data==item.data:
                return node
            node=node.next
    def insert(self,item,position):
        nodeN=self.getItem(DNode(position))
        nodeP=nodeN.previous
        item.next=nodeN
        nodeP.next=item
        nodeN.previous=item
        item.previous=nodeP

    def delete(self,item):
        item=self.getItem(DNode(item))
        nodeP=item.previous
        nodeN=item.next
        nodeP.next = nodeN
        nodeN.previous=nodeP
'''        
queue = Queue()
queue.add(DNode('Raj'))
queue.add(DNode('Zed'))
queue.add(DNode('Joanna'))
queue.insert(DNode("Doug"),"Zed")

# n1 = queue.head 
# n2 = n1.next 
# n3 = n2.next 
# print("Traversing the queue")
# print(n1.data)
# print(n2.data)
# print(n3.data)
# print()
# #insert
# queue.insert(DNode('Linh'),'Zed')
# node = queue.head
# while node.next != None:
#     print(node.data)
#     node= node.next
# print(node.data)
# print()
# #delete
# queue.delete('Linh')
node = queue.head
while node.next != None:
    print(node.data)
    node= node.next
print(node.data)
'''

#The professor changed this files and added one sort of __str__ method
# Does anyone have it ? 
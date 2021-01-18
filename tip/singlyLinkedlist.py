class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None

class SLL:
    def __init__(self):
        #the attribute self.head represents the first node in a sequence of nodes
        self.head = None
    
    def addToBack(self, valueInput):
        #create a new node
        newnode = Node(valueInput)
        if self.head == None:
            self.head = newnode
        else:
            #create a runner and loop it until it points to the last node in the SLL
            runner = self.head
            while runner.next != None:
                #increments runner by one node
                runner = runner.next
            runner.next = newnode

        return self
    
    def display(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next

sll1 = SLL()
sll1.addToBack(5).addToBack(10).addToBack(15).display()


#creating node objects below
# node1 = Node(15)
# node2 = Node(13)
# node3 = Node(12)
# node4 = Node(23)

# node1.next = node2
# node2.next = node3
# node3.next = node4

# print(node1.next.value) #13
# print(node1.next.next)


# sll1 = SLL()
# sll1.head = node1
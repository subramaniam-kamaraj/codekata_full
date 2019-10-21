class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertatbeg(self, value):
        if (self.head == None):
            self.head = self.tail = Node(value)
        else:
            newnode = Node(value)
            newnode.next = self.head
            self.head = newnode

    def insertatend(self, value):
        if (self.head == None):
            self.head = self.tail = Node(value)
        else:
            newnode = Node(value)
            self.tail.next = newnode
            self.tail = newnode

    def insertatpos(self, position, value):
        temp = self.head
        for i in range(1, position - 1):
            temp = temp.next
        newnode = Node(value)
        newnode.next = temp.next
        temp.next = newnode
        temp = None

    def display(self):
        temp = self.head
        while (temp is not None):
            print(temp.data, end=" ")
            temp = temp.next


s = SLL()
s.insertatbeg(10)
s.insertatbeg(20)
s.insertatbeg(30)
s.insertatend(89)
s.insertatend(90)
s.insertatpos(2, 56)
s.insertatpos(3, 78)
s.display()
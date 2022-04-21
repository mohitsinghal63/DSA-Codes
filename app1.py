class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.start=None
    def create(self):
        data=int(input("enter data: "))
        n=node(data)
        if self.start is None:
            self.start=n
        else:
            ptr=self.start
            while ptr.next is not None:
                ptr=ptr.next
            ptr.next=n
            n.prev=ptr
    def countnodes(self):
        if self.start is None:
            return 0
        else:
            ptr=self.start
            count=1
            while ptr.next is not None:
                ptr=ptr.next
                count+=1
            return count
    def insert(self):
        n=self.countnodes()
        pos=int(input("enter position: "))
        if pos<=0:
            pos=1
        if pos>n+1:
            pos=n+1
        data = int(input("enter data: "))
        n = node(data)
        if pos==1:
            n.next=self.start
            self.start=n
        else:
            ptr=self.start
            i=1
            while i<pos-1:
                ptr=ptr.next
                i=i+1
            ptr1=ptr.next
            n.next=ptr.next
            ptr.next=n
            n.prev=ptr1.prev
            ptr1.prev=n


    def delete(self):
        n=self.countnodes()
        pos=int(input("enter position: "))
        if pos<=0:
            pos=1
        if pos>n:
            pos=n
        if pos==1:
            self.start=self.start.next
            self.start.prev=None
        elif pos==n:
            ptr=self.start
            i=1
            while i<pos-1:
                ptr=ptr.next
                i=i+1
            ptr.next=None

        else:
            ptr=self.start
            i=1
            while i<pos:
                ptr=ptr.next
                i=i+1
            ptr.next.prev=ptr.prev
            ptr.prev.next = ptr.next
    def update(self):
        pos=int(input("enter position: "))
        ptr=self.start
        i=1
        while i<pos:
            ptr=ptr.next
            i=i+1
        ptr.data=int(input("enter new data: "))


    def traverse(self):
        ptr=self.start
        while ptr is not None:
            print(ptr.data)
            ptr=ptr.next
    def backward_traverse(self):
        ptr=self.start
        while ptr.next is not None:
            ptr=ptr.next
        while ptr is not None:
            print(ptr.data)
            ptr=ptr.prev










l=LinkedList()
n=int(input("enter no: "))
for i in range(n):
    l.create()
l.backward_traverse()
l.update()
l.traverse()
#l.backward_traverse()
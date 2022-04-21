class node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Linkedlist():
    def __init__(self):
        self.start=None
    def create(self):
        data=int(input("enter data: "))
        n=node(data)
        if self.start is None:
            self.start=n
            n.next=self.start
            n.prev=self.start
        else:
            ptr=self.start
            while ptr.next!=self.start:
                ptr=ptr.next
            ptr.next=n
            n.next=self.start
            n.prev=ptr
    def countnodes(self):
        if self.start is None:
            return 0
        else:
            ptr=self.start
            count=1
            while ptr.next!=self.start:
                count+=1
                ptr=ptr.next
            return count
    def insert(self):
        m=self.countnodes()
        pos=int(input("enter position: "))
        while pos<=0 or pos>m+1:
            print("enter valid position")
            pos=int(input("enter position: "))
        data=int(input("enter data: "))
        n=node(data)
        if pos==1:
            ptr=self.start
            while ptr.next!=self.start:
                ptr=ptr.next
            ptr.next=n
            self.start.prev=n
            n.next=self.start
            n.prev=ptr
            self.start=n
        elif pos<m+1:
            ptr=self.start
            i=1
            while i<pos-1:
                ptr=ptr.next
                i=i+1
            n.next = ptr.next
            n.prev=ptr
            ptr.next.prev=n
            ptr.next=n
        if pos==m+1:
            ptr=self.start
            i=1
            while i<pos-1:
                ptr=ptr.next
                i=i+1
            n.prev=ptr
            n.next=ptr.next
            ptr.next=n
    def delete(self):
        m=self.countnodes()
        pos=int(input("enter position: "))
        while pos<=0 or pos>m:
            print("enter valid position")
            pos=int(input("enter position: "))

        if pos==1:
            ptr=self.start
            while ptr.next!=self.start:
                ptr=ptr.next
            ptr.next=self.start.next
            self.start.prev = ptr
            self.start=self.start.next

        ptr=self.start
        if pos<m:
            i=1
            while i<pos:
                ptr=ptr.next
                i=i+1
            ptr.prev.next=ptr.next
            ptr.next.prev=ptr.prev
        if pos==m:
            i=1
            while i<pos:
                ptr=ptr.next
                i=i+1
            ptr.prev.next=ptr.next
            self.start.prev=ptr.prev

    def traverse(self):
        if self.start is None:
            print("Linkedlist is empty")
            return
        ptr=self.start
        if ptr.next!=self.start:
            while ptr.next != self.start:
                print(ptr.data)
                ptr = ptr.next
            if ptr.next==self.start:
                print(ptr.data)
    def backward_traverse(self):
        ptr = self.start
        while ptr.next!=self.start:
            ptr=ptr.next
        while ptr!=self.start:
            print(ptr.data)
            ptr=ptr.prev
            if ptr==self.start:
                print(ptr.data)




l=Linkedlist()
n=int(input("enter nodes: "))
for i in range(n):
    l.create()
l.backward_traverse()
l.traverse()
l.insert()
l.traverse()
l.delete()
l.traverse()
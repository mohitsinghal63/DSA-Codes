class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.start=None
    def create(self):
        data=int(input("enter data: "))
        n=node(data)
        if self.start is None:
            self.start=n
            n.next=self.start
        else:
            ptr=self.start
            while ptr.next !=self.start:
                ptr=ptr.next
            ptr.next=n
            n.next=self.start
    def countnodes(self):
        if self.start is None:
            return 0
        else:
            count=1
            ptr=self.start
            while ptr.next!=self.start:
                ptr=ptr.next
                count+=1
            return count
    def traverse(self):
        ptr = self.start
        if ptr.next !=self.start:
            while ptr.next !=self.start:
                print(ptr.data)
                ptr=ptr.next
        if ptr.next==self.start:
                print(ptr.data)
    def insert(self):
        n=self.countnodes()
        pos=int(input("enter position: "))
        if pos<=0:
            pos=1
        if pos>n+1:
            pos=n+1
        data=int(input("enter data: "))
        n=node(data)
        if pos==1:
            self.start=n
            n.next=self.start
        else:
            ptr=self.start
            i=1
            while i<pos-1:
                ptr=ptr.next
                i=i+1
            n.next=ptr.next
            ptr.next=n
    def delete(self):
        n=self.countnodes()
        pos=int(input("enter position: "))
        if pos<=0:
            pos=1
        if pos>n:
            pos=n

        if pos==1:
            ptr=self.start
            while ptr.next !=self.start:
                ptr=ptr.next
            ptr.next=self.start.next
            self.start=self.start.next
        else:
            ptr=self.start
            i=1
            while i<pos-1:
                ptr=ptr.next
                i=i+1
            ptr.next=ptr.next.next


l=Linkedlist()
n=int(input("enter nodes: "))
for i in range(n):
    l.create()
l.traverse()
l.insert()
l.traverse()
l.delete()
l.traverse()
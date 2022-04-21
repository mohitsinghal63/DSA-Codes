class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.start=None
        self.end=None
    def create(self):
        data=int(input("enter data: "))
        n=node(data)
        if self.start is None:
            self.start=n
            self.end=n
        else:
            ptr=self.start
            while ptr.next is not None:
                ptr=ptr.next
            ptr.next=n
            self.end=n
    def countnodes(self):
        if self.start is None:
            return 0
        else:
            count=1
            ptr=self.start
            while ptr.next is not None:
                ptr=ptr.next
                count+=1
            return count
    def traverse(self):
        ptr = self.start
        while ptr is not None:
            print(ptr.data)
            ptr=ptr.next
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
            n.next = self.start
            self.start=n
        elif pos==n+1:
            self.end.next=n
            self.end=n
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
            self.start=self.start.next
        elif pos==n:
            ptr = self.start
            i = 1
            while i < pos - 1:
                ptr = ptr.next
                i = i + 1
            ptr.next = ptr.next.next
            self.end=ptr
        else:
            ptr=self.start
            i=1
            while i<pos-1:
                ptr=ptr.next
                i=i+1
            ptr.next=ptr.next.next

    def delete_data(self):
        flag=0
        datas=int(input("enter data which you have deleted: "))
        ptr=self.start
        if self.start.data==datas:
            self.start=self.start.next
        else:
            while ptr.next is not None:
                if ptr.next.data==datas:
                    ptr.next=ptr.next.next
                    flag=1
                    break
                ptr = ptr.next
            if flag==0:
                print("data is not present")
    def


    def reverse(self):
        prev=None
        ptr1=self.start
        while ptr1 is not None:
            next=ptr1.next
            ptr1.next=prev
            prev=ptr1
            ptr1=next
        self.start=prev
    def find_middle(self):
        if n%2!=0:
            ptr=self.start
            ptr1=self.start
            while ptr1.next is not None:
                ptr1=ptr1.next.next
                ptr=ptr.next
            print(ptr.data)
        else:
            ptr=self.start
            ptr1=self.start
            while ptr1.next.next is not None:
                ptr1=ptr1.next.next
                ptr=ptr.next
            print(ptr.data)
            print(ptr.next.data)
    def create_sorted(self):
        data = int(input("enter data: "))
        n = node(data)
        if self.start is None:
            n.next=self.start
            self.start = n
        else:
            ptr=self.start
            ptr1=None
            while ptr is not None and ptr.data<n.data:
                ptr1=ptr
                ptr=ptr.next
            n.next=ptr1.next
            ptr1.next=n




l=Linkedlist()
n=int(input("enter nodes: "))
for i in range(n):
    l.create_sorted()
l.delete_data()
l.traverse()
#l.reverse()
#l.find_middle()



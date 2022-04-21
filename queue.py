queue=[]
def enqueue(ch):
     queue.append(ch)
def dequeue():
    qu1=queue[0]
    queue.remove(queue[0])
    return qu1
def front():
    return queue[0]
def rear():
    return queue[-1]
def isempty():
    if len(queue)==0:
        return True
    return False



arr=[5,4,8,9,2,3,1]
n=len(arr)
for i in range(n):
    enqueue(min(arr))
    arr.remove(min(arr))

print(queue)
print(front())
print(dequeue())
print(front())
print(rear())
print(isempty())
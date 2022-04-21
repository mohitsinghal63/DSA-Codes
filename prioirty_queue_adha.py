q1=[]
q2=[]
q3=[]
def enqueue(ch,pr):
    if pr==1:
        q1.append(ch)
    elif pr==2:
        q2.append(ch)
    elif pr==3:
        q3.append(ch)
#def dequeue():
 #   qu1=queue[0]
  #  queue.remove(queue[0])
   # return qu1
#def front():
#    return queue[0]
#def rear():
#    return queue[-1]
#def isempty():
#    if len(queue)==0:
#        return True
#    return False



arr=['A','B','C','D','E','F','G']
pri=[1,2,3,2,3,1,2]
n=len(arr)
for i in range(n):
    if pri[i]==1:
        enqueue(arr[i],1)
    elif pri[i]==2:
        enqueue(arr[i],2)
    elif pri[i]==3:
        enqueue(arr[i],3)

print(q1)

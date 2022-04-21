arr=[1,2,3,-2,5]
n=len(arr)
count=0
max_sum=0
for i in arr:
    if i<0:
       count+=1
if count>1:
    cls=1
    for i in arr:
        if cls<=count-(n-1):
            max_sum=max_sum+i
            cls+=1
        else:
            break
if count<=1:
    for i in arr:
        max_sum=max_sum+i
print(max_sum)


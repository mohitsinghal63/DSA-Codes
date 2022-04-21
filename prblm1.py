arr=[-1,-2,-3,-4]
total_sum=sum(arr)
sum1=arr[0]
for i in range(1,len(arr)):
    if total_sum>=sum1:
        sum1=sum1+arr[i]
print(sum1)

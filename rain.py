'''arr=[3,0,0,2,0,4]
n=len(arr)
maxi=arr[0]
for i in range(1,n):
    if arr[i]>maxi:
        maxi=arr[i]
arr.remove(maxi)
# Next Part:-
m=len(arr)
second_maxi=arr[0]
for i in range(1,m):
    if arr[i]>second_maxi:
        second_maxi=arr[i]
arr.append(maxi)
# final Solution:-
sum=0
for i in range(len(arr)):
    if maxi==second_maxi:
        sum=0
        break
    else:
        if arr[i]<second_maxi:
            sum=sum+(second_maxi-arr[i])
print(sum)'''
'''def max_user(arr,start,end):
    max_num=arr[start]
    for i in range(start,end+1):
        if arr[i]>max_num:
            max_num=arr[i]
    return max_num'''
def water(arr,n):
    temp=0
    lmax=arr[0]
    rmax=[0]*n
    rmax[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        if arr[i]>rmax[i+1]:
            rmax[i]=arr[i]
        else:
            rmax[i]=rmax[i+1]

    for i in range(n):
        if arr[i]>lmax:
            lmax=arr[i]

        if lmax<rmax[i]:
            temp=temp+(lmax-arr[i])
        else:
            temp=temp+(rmax[i]-arr[i])
    return temp

arr=[3,0,0,2,0,4]
result=water(arr,len(arr))
print(result)




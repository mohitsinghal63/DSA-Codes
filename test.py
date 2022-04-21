#s= 1 2 3 4 5
   #2     5
   #3   5
   #4 5
   #5*\
'''n=5
for i in range(1,n+1):
    print(i,end=' ')
    for j in range(i+1,n+1):
        if i==1:
            print(j,end=' ')
        if i>1:
            if (j==2) or (j==n):
                print(j,end=' ')
            else:
                print(" ",end=" ")

    print()'''

# CONVERSION OF ARAAY:

arr=[4,3,7,8,6,2,1]
n=len(arr)
for i in range(n):
    if i%2==0 and i<n-1:
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
        else:
            arr[i]=arr[i]
    elif i==n-1:
        arr[i]=arr[i]
    else:
        if arr[i]<arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]

        else:
            arr[i]=arr[i]
print(arr)






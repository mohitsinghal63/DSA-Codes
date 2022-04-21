'''***
***
***
***
***
n=int(input("enter number: "))
for i in range(n):
    print('*'*3)'''
'''*
    **
    *
    **
    ***
n=int(input("enter value: "))
for i in range(n):
    if i%2==0 and i<n-1:
        print('*'*1)
    elif i==n-1:
        print('*'*3)
    else:
        print('*'*2)'''
'''***
    **
    *
    **
    *
n=int(input("enter value: "))
for i in range(n):
    if i==0:
        print('*'*3)
    elif i%2!=0:
        print('*'*2)
    else:
        print('*'*1)'''
'''1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
n=int(input("enter value: "))
for i in range(1,n+1):
    print(1,end=' ')
    if i>0:
        for j in range(2,i+1):
            print(j,end=' ')
    print()'''
'''*
**
*
**
** *
**
*
**
*
n=int(input())
for i in range(n):
    if i==4:
        print('*'*3)
    elif i%2==0:
        print('*'*1)
    else:
        print('*'*2)'''
'''*
       *
      ***
     ***
    ***
n=int(input())
for i in range(n):
    if i==0 or i==1:
        print('*'*1)
    else:
        print('*'*3)'''
'''*
* *
* * *
* * * *
* * * * *
n=int(input())
for i in range(1,n+1):
    print('*'*i)'''
'''* * * * *
      * * * *
       * * *
        * *
         *
n=int(input())
for i in range(n):
    print('*'*(n-i))'''
'''* * * * *
* * * *
* * *
* *
*
*
* *
* * *
* * * *
* * * * *
n=int(input())
for i in range(n):
    print('*'*(n-i))
for i in range(1,n+1):
    print('*'*i)'''
'''     *
        * *
       *   *
      *     *
     ***'''
'''n=int(input())
for i in range(1,n+1):
    if i==1:
        print('*')
    elif i==n:
        print('*'*3)'''
'''s1='triangle'
n=len(s1)
s2='integral'
m=len(s2)
count=0
if n!=m:
    print("no. is not anagram.")
else:
    for i in range(n):
        if s1[i] in s2:
            count+=1
    if count==m:
        print("no. is anagram.")
    else:
        print("no. is not anagram.")'''
'''def alternate(arr,n):
    arr1=[]
    for i in range(n):
        if arr[i]>0:
            arr1.append(arr[i])
            arr.remove(arr[i])
            break
    for i in range(n-1):
        if arr[i]<0:
            arr1.append(arr[i])
            if arr[i+1]>=0:
                arr1.append(arr[i+1])
            if arr[i-1]>=0:
                arr1.append(arr[i-1])
    print(arr1)
    return 0

arr=[-5,-2,5,2,4,7,1,8,0,-8]
n=len(arr)
result=alternate(arr,n)
print(result)'''

'''def sum_pairs(arr,n,k):
    count=0
    s=set(arr)
    for i in range(n):
        s.remove(arr[i])
        for j in s:
            if (arr[i]+j) %k==0:
                count+=1
                continue
    return count

arr=[8,13,40,80,64,53,57]
n=len(arr)
k=3
result=sum_pairs(arr,n,k)
print(result)'''

'''def truck(arr1,arr2,n):
    s=set(arr2)
    for i in range(n):
        







arr1=[4,6,7,4]
arr2=[6,5,3,5]
n=len(arr1)
result=truck(arr1,arr2,n)'''

'''def sun(arr,n):
    count=0
    for i in range(n):
        if i==0:
            count+=1
        if i>0:
            if arr[i-1]<arr[i]:
                count+=1
    return count

arr=[7,4,8,2,9]
n=len(arr)
result=sun(arr,n)
print(result)'''

      1
    1 2 1
   1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
n=5
i=1
while i!=n+1:
    if i==1:
        print(1,end=' ')
        i=i+1
    elif i>1:
        for j in range(i,n):
            if i==j:
                x=1
                print(x,j,x)
                i=i+1
                break

    x = 0
    print(i,x+1,end=' ')
    for j in range(1,n):
        print()

    print()








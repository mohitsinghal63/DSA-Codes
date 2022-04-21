'''n=4
arr=[1,5,11,5]
sum=0
flag=0
for i in range(n):
    result=arr[i]
    arr.remove(arr[i])
    for j in range(n-1):
        sum=sum+arr[j]
    arr.append(arr[i])
    if result==sum:
        print("yes")
        flag=1
        break
if flag==0:
    print("no")'''

'''s='chandrapal'
result=''
result1=set(result)
for i in s:
    if i  in result1:
        break
    else:
        result=result+i
        result1.add(i)
print(result)'''

'''def multiple(arr,n):
    arr1=[]
    arr2=[]
    for i in range(n):
        if arr[i]%10==0:
            arr1.append(arr[i])
    m=len(arr1)
    if len(arr1)==0:
        return -1
    for i in range(m+1):
        count = 0
        for j in str(arr[i]):
            if j=='0':
                count+=1
        arr2.append(count)
    for i in arr2:
        if i==0:
            arr2.remove(i)
    ans=max(arr2)
    for i in range(len(arr1)):
        for j in range(i,len(arr2)):
            if arr2[j]==ans:
                return arr1[i]
            else:
                break
arr=[10,20,3000,9999,200]
n=len(arr)
result=multiple(arr,n)
print(result)'''

'''n=5
x=1
for i in range(n+1):
    if i==1:
        print(' ',x,' '*3,end=' ')
    elif i==n:
        print(1,2,3,4,5,end=' ')
    if i>1 and i<n:
        for j in range(i,n):
            print(' '*2,x,' '*i,j,end=' ')
            break
    print()'''
'''arr=[[1,2,3,4],3,4,[5],[7,5]]
n=len(arr)
sum=0
for i in range(n):
    if type(arr[i])==int:
        sum=sum+arr[i]
    else:
        for j in arr[i]:
            sum=sum+j
print(sum)'''
'''arr=[5,-5,-2,2,4,7,1,8,0,-8]
n=len(arr)
arr1=[]
maxi=0
mini=0
cnt1=0
cnt2=0
for i in range(n):
    if arr[i]>0:
        arr1.append(arr[i])
        arr.remove(arr[i])
        break
for i in range(n-1):
    if arr[i]>=0:
        maxi+=1
    else:
        mini+=1

for i in range(n-1):
    if cnt1 < mini:
        if arr1[i]>=0:
            for j in range(n-1):
                if arr[j]<0:
                    arr1.append(arr[j])
                    arr.remove(arr[j])
                    cnt1+=1
                    break
    else:
        arr1.append(arr[i])
    if cnt2<maxi:
        if cnt2 < maxi:
            if arr1[i]<0:
                for k in range(n-1):
                    if arr[k]>=0:
                        arr1.append(arr[k])
                        arr.remove(arr[k])
                        break
    else:
        arr1.append(arr[i])
print(arr1)'''

'''arr=[20,15,17,14,12]
n=len(arr)
for i in range(1,n):
    mini=i-1
    for j in range(i,n):
        if arr[mini]>arr[j]:
            mini=j
    arr[mini],arr[i-1]=arr[i-1],arr[mini]
    i=i+1
print(arr)'''

'''arr=[4,5,2,25]
n=len(arr)
temp=[]
flag=0
for i in range(n):
    for j in range(i+1,n):
        if arr[i]<arr[j]:
            temp.append(arr[j])
            flag=1
            break
    if flag==0:
        temp.append(-1)
    if i==n-1:
        temp.append(-1)

print(temp)'''

'''arr=[34,3,31,98,92,23]
n=len(arr)
arr1=[]
mini=arr[0]
result=[0]*n
m=len(result)
for i in range(m):
    for i in range(n):
        if arr[i]<mini:
            mini=arr[i]
    result[i]=mini
    arr.remove(mini)'''

'''arr=[34,3,31,98,92,23]
n=len(arr)
result=[0]*n
m=len(arr)
for i in range(m):
    result[i]=min(arr)
    arr.remove(min(arr))
print(result)'''

'''arr=[1,1,2,3,4,2,1]
n=len(arr)
freq=[0]*n
m=len(freq)
for i in range(m):
    cnt=0
    freq[i]=arr[i]
    for j in range(n):
        if freq[i] in arr:
            cnt+=1
    freq[i]=cnt
print(freq)'''

arr=[5,4,3,4,5]
n=len(arr)
l=[0]*n
r=[0]*n
flag=0
for i in range(len(l)):
    maxi=arr[0]
    for j in range(n):
        if arr[j]==0:
            flag=1
            break
        else:
            if arr[j]












































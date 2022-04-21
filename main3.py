'''s1='listen'
s2='silent'
s3=sorted(s1)
s4=sorted(s2)
count=0
if len(s1)!=len(s2):
    print("not anagram")
else:
    set1=set(s4)
    for i in range(len(s3)):
        if s3[i] in set1:
            count+=1
    if count==len(s3):
        print("anagram")
    else:
        print("not anagram")'''

'''arr=[-56,0,87,5,4,6]
n=len(arr)
for i in range(1,n):
    if arr[i]>0:
        mini=arr[i]
        break
for i in range(n):
    if arr[i]>0 and arr[i]<mini:
        mini=arr[i]
print(mini)
for i in range(1,n):
    if arr[i]>0:
        maxi=arr[i]
        break
for i in range(n):
    if arr[i]>0 and arr[i]>maxi:
        maxi=arr[i]
print(maxi)

for i in range(1,(maxi+2)):
    if i in arr:
        i+=1
    else:
        print(i)
        break'''
'''arr=[3,2,1,2,1,4,5,8,6,7,4,2]
n=len(arr)
arr1=[]
result=[]
for i in range(n):
    if arr[i] not in arr1:
        maxi=0
        for j in range(n-1,i,-1):
            if arr[i]==arr[j]:
                if maxi<(j-i):
                    maxi=j-i
        result.append(maxi)
        arr1.append(arr[i])
print(max(result))'''
'''n=4
flag=0
for i in range(1,n+1):
    num=i
    print(" "*(n-i),end="")
    for j in range(1,2*i):
        print(num,end="")
        if num!=1:
            num=num-1
        else:
            num=num+1
    print()'''
'''n=6
for i in range(n,0,-1):
    num=65
    for j in range(1,i+1):
        print(chr(num)," ",end="")
        num=num+1
    print()
for i in range(1,n+1):
    num=65
    for j in range(1,i+1):
        print(chr(num)," ",end="")
        num=num+1
    print()'''
'''n=5
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    num=(n-i)+1
    for j in range(1,i+1):
        print(num," ",end="")
        num=num+1
    print()
for i in range(2,n+1):
    print(" "*(n-i),end="")
    num=(n-i)+1
    for j in range(1,i+1):
        print(num," ",end="")
        num=num+1
    print()'''
'''n=5
for i in range(1,n+1):
    num=1
    for j in range(1,i+1):
        print(num,end="")
        num=abs(num-1)
    print()'''
'''n=5
num1=1
for i in range(1,n+1):
    num=num1
    for j in range(1,n+1):
        print(num1,end="")
        num1=abs(num1-1)

    print()
    num=abs(num1-1)'''


'''def __gcd(a, b):
    if (b == 0): return a;
    return __gcd(b, a % b);



def maxSubarrayLen(arr, n):

    maxLen = 0;
    for i in range(n):
        a=arr[i]
        for j in range(i, n):
            gcd1=[]
            gcd1.append(a)
            gcd1.append(arr[j])
            gcd2 = __gcd(a, arr[j]);
            if (gcd2>= len(gcd1)):
                maxLen = len(gcd1)
            else:
                break;
    print(maxLen);


arr = [4,1,2,4,8];
N = len(arr)
maxSubarrayLen(arr, N);'''

'''def push(ele):
    arr.append(ele)
    global top
    top+=1
def pop():
    global top
    top-=1
    return arr.pop(top+1)
def peek():
    global top
    return arr(top)
def is_empty():
    global top
    if top==-1:
        print('true')
    else:
        print('false')
def traverse():
    global top
    for i in range(top,-1,-1):
        print(arr[i])

arr=[]
top=-1
push(10)
print(traverse())'''


arr=[100,80,60,70,60,75,85]
n=len(arr)
stack=[]
arr1=[]
top=-1
for i in range(0,n):
    cnt = 1
    if i==0:
        arr1.append(cnt)
        stack.append(i)
        top=top+1
    else:
        if arr[i]<arr[stack[top]]:
            arr1.append(cnt)
            stack.append(i)
        else:
            while len(stack[top])>=0 and arr[i] > arr[stack[top]]:
                top = top - 1
                stack.pop()

            arr1.append(i-top)

print(arr1)




























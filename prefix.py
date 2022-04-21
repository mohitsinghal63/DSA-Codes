arr=['chandrapal','chandler','characterstics','channelization']
n=len(arr)
arr.sort()
length=len(arr[0])
temp=''
temp1=''
result=""
flag=0
for i in range(1):
    for j in range(length):
        if arr[i][j]==arr[i+1][j]:
            temp=temp+arr[i][j]

for i in range(2,n-1):
    for j in range(len(arr[2])):
        if arr[i][j]==arr[i+1][j]:
            temp1=temp1+arr[i][j]
for i in range(len(temp)):
    for j in range(len(temp1)):
        if temp[i]==temp1[j]:
            result=result+temp[i]
            flag=1
if flag==0:
    result=-1
print(result)






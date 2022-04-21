'''def zero(arr,n,ele):
    for i in range(n):
        if arr[i]==ele:
            arr.remove(ele)
            arr.append(0)
    return arr
arr=[14,20,14,30,14,75,24,14]
ele=14
result=zero(arr,len(arr),ele)
print(result)'''
arr=[1,8,2,3,4,5,7,20]
flag=0
arr1=[]
for i in arr:
    if i==1:
        arr.remove(i)
        arr.append(i)
    if i>1:
        for j in range(2,i):
            if i%j==0:
                flag=1
                break
    if flag==0:
        arr.remove(i)
        arr1.append(i)
    else:
        arr.remove(i)
        arr.append(i)
print(arr)


















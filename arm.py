'''arr=[3,4,1,9,56,7,9,12]
n=len(arr)
m=5
diff=9999999999
arr.sort()
for i in range(0,n-(m+1)):
    mini=arr[i]
    maxi=arr[i]
    for j in range(i+1,m+i):
        if arr[j]>maxi:
            maxi=arr[j]
        if arr[j]<mini:
            mini=arr[j]
    if diff > (maxi-mini):
        diff=maxi-mini
print(diff)'''



# CHOCOLATE DISTRIBUTION PROMBLEM:

def chocolate(arr,n,m):
    arr.sort()
    result=99999
    for i in range((n-m)+1):
        if i<n-m:
            max_=arr[m+i-1]
            min_=arr[i]
            if result>(max_-min_):
                result=max_-min_
    return result
arr=[7,3,2,4,9,12,56]
n=len(arr)
m=3
print(chocolate(arr, n, m))


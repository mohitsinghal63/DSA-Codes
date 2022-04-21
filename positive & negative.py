def num(arr,n):
    arr1=[]
    for i in range(n):
        if i==n-1:
            arr1.append(0)
        else:
            p_cnt=0
            n_cnt=0
            for j in range(i+1,n):
                if arr[j]<0:
                    n_cnt=n_cnt+abs(arr[j])
                if arr[j]>=0:
                    p_cnt=p_cnt+arr[j]
            arr1.append(abs(p_cnt-n_cnt))
    return arr1
    












arr=[1,-1,2,3,-2]
n=len(arr)
print(num(arr,n))
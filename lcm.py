def lcm(a,b):
    if b>a:
        res=0
        i=1
        while True:
            res=b*i
            if res%b==0 and res%a==0:
                return res
            i=i+1
    if a>b:
        res=0
        i=1
        while True:
            res=a*i
            if res%b==0 and res%a==0:
                return res
            i=i+1
        
            
            
        
a,b=int(input()),int(input())
print(lcm(a,b))
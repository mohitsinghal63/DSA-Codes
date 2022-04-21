def hcf(a,b):
    if a<b:
        for i in range(a,0,-1):
            if a%i==0 and b%i==0:
                return i
            
    elif b<a:
        for i in range(b,0,-1):
            if a%i==0 and b%i==0:
                return i
        
        
    

a=36
b=60
print(hcf(a,b))
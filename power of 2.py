def power(n):
    if n%2!=0 and n==0:
        return False
    else:
        while(n!=1):
            if n%2!=0:
                return False
            else:
                n=n//2
        return True
        
    
    




n=int(input())
print(power(n))
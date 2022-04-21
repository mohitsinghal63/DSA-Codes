def k_anag(s1,s2,k):
    count=0
    s3=list(s1)
    s4=list(s2)
    if len(s3)!=len(s4):
        return False
    else:
        print(s3)
        for i in range(len(s3)):
            if s3[i]!=s4[i]:
                s3[i]=s4[i]
                count+=1
        if s3==s4 and k==count-1:
            return True
        else:
            return False
                
            
    


s1='fodr'
s2='gork'
k=2
print(k_anag(s1,s2,k))
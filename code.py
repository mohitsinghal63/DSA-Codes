s1='abcd'
s4=s1*2
s2='cdab'
s3=list(s1)
n=len(s2)
for i in range(0,n-1):
    if i==0:
        s3[i]=s3[n-1]
    else:
        s3[i]=s3[i-1]
print(''.join(s3))
print(s4)

s5=s4.find('cdab')
if s5==-1:
    print('False')
else:
    print('TRUE')


        
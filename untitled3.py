s = 'zzzoooooo'
n=len(s)
count_z=0
count_o=0
for i in range(n):
    if s[i]=='z':
        count_z=count_z+1
    else:
        count_o=count_o+1
        
if 2*count_z==count_o:
    print("True")
else:
    print("False")
x=""
a=int(input("Enter a no.:"))
b=a//2
c=a%2
if c==0:
        x=x+"0"
else:
        x=x+"1"
while b!=0:
    if c==0:
        x=x+"0"
        b=b//2
        c=b%2
    else:
        x=x+"1"
        b=b//2
        c=b%2
no=[]
z=""
b=len(x)-1
for i in x:
    no.append(i)
for i in range(b,-1,-1):
    d=no[i]
    z=z+d
print(z)
    

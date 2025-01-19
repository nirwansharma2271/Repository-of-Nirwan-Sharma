a=input("Enter a no.:")
b=len(a)
z=0
for i in range(0,b):
    j=len(a)-1-i
    d=int(a[i])
    if d==1:
        z=z+1*2**j
    else:
        z=z+0
print(z)

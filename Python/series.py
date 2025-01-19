x=int(input("Enter the number.:"))
n=int(input("Enter the number.:"))
z=1
for i in range(1,n+1):
    b=x**i
    if i==n:
        print(b)
    elif i==1:
        print("1+",x,end="+")
    else:
        print(b,end="+")
    z+=b
print("SUM:",z)
z=0
b=x**2
for i in range(1,n+1):
    if i==n:
        print(str(b)+"/"+str(i))
    else:
        print(str(b)+"/"+str(i),end="+")
    z+=b/i
print("SUM:",z)

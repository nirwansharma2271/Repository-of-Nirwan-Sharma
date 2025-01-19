print("Welcome to odd even ")
low=int(input("enter the lower limit:"))
high=int(input("enter the higher limit"))
even=0
odd=0
for i in range(low,high+1):
    if i%2==0:
        even+=i
    else:
        odd+=i
else:
    print("Even no.s sum =",even)
    print("odd no.s sum =",odd)
        

 

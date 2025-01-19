a=int(input("Enter the first no.:"))
b=int(input("Enter the second no.:"))
c=int(input("Enter the third no.:"))
d=int(input("Enter the fourth no.:"))
e=int(input("Enter the fifth no.:"))
if a<b and a<c and a<d and a<e:
    print("a:",a,"is smaller")
elif b<a and b<c and b<d and b<e:
    print("b:",b,"is smaller")
elif c<a and c<b and c<d and c<e:
    print("c:",c,"is smaller")
elif d<a and d<c and d<b and d<e:
    print("d:",d,"is smaller")
elif e<a and e<c and e<d and e<b:
    print("e:",e,"is smaller")
else:
    print("error")

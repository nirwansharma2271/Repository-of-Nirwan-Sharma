print("If this algorithm is used where:\nif x is a odd no. then use 3x+1 or else use x/2 and then repeat it many a times.\nThe answer before it starts looping will be 1")
i=0
while i != 1:
    e=input("Continue?(y/n):")
    if e.lower() == "y":
        a=float(input("enter any number:"))
        c=0
        d=0
        b=0
        print(a)
        while a!=1:
            if a%2==0:
                c+=1
                b+=1
                a=a/2
                print(b,":",a,"(used x/2)")
            else:
                d+=1
                b+=1
                a=3*a+1
                print(b,":",a,"(used 3x+1)")
        else:
            print("SUCCESS")
            print("3x+1 is used",d,"times","x/2 is used",c,"times")
else:
    print("exit")

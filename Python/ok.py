print("Welcome to Python:Variables ")
print("Code for the options:","\n","S for string","\n","I for Integer", "\n","F for float", "\n" )
opt=input("Enter the type of value to assign variable:")
no=int(input("Enter the no. of variables:"))

if no==1:
    if opt=="I":
        A=int(input("Enter the value to assign Variable A:"))
    elif opt=="F":
        A=float(input("Enter the value to assign Variable A:"))
    elif opt=="S":
        A=input("Enter the value to assign Variable A:")
    else:
        print("wrong code enter")
        
elif no==2:
    if opt=="I":
        A=int(input("Enter the value to assign Variable A:"))
        B=int(input("Enter the value to assign Variable B:"))
    elif opt=="F":
        A=float(input("Enter the value to assign Variable A:"))
        B=float(input("Enter the value to assign Variable B:"))
    elif opt=="S":
        A=input("Enter the value to assign Variable A:")
        B=input("Enter the value to assign Variable B:")
    else:
        print("wrong code enter")
        
elif no==3:
    if opt=="I":
        A=int(input("Enter the value to assign Variable A:"))
        B=int(input("Enter the value to assign Variable B:"))
        C=int(input("Enter the value to assign Variable C:"))
    elif opt=="F":
        A=float(input("Enter the value to assign Variable A:"))
        B=float(input("Enter the value to assign Variable B:"))
        C=float(input("Enter the value to assign Variable C:"))
    elif opt=="S":
        A=input("Enter the value to assign Variable A:")
        B=input("Enter the value to assign Variable B:")
        C=input("Enter the value to assign Variable C:")
    else:
        print("wrong code enter")
        
elif no==4:
    if opt=="I":
        A=int(input("Enter the value to assign Variable A:"))
        B=int(input("Enter the value to assign Variable B:"))
        C=int(input("Enter the value to assign Variable C:"))
        D=int(input("Enter the value to assign Variable D:"))
    elif opt=="F":
        A=float(input("Enter the value to assign Variable A:"))
        B=float(input("Enter the value to assign Variable B:"))
        C=float(input("Enter the value to assign Variable C:"))
        D=float(input("Enter the value to assign Variable D:"))
    elif opt=="S":
        A=input("Enter the value to assign Variable A:")
        B=input("Enter the value to assign Variable B:")
        C=input("Enter the value to assign Variable C:")
        D=input("Enter the value to assign Variable D:")
    else:
        print("wrong code enter")
        
else:
    print("maximum limit reached")
    
if opt=="S":
    ans=input("Concatenation or Replication?:")
    if ans=="Concatenation":
        if no==1:
            print(A)
        elif no==2:
            print(A+" "+B)
        elif no==3:
            ans=input("All or Custom:")
            if ans=="All":
                print(A+" "+B+" "+C)
            elif ans=="Custom":
                ans=input("A should be joined with:")
                if ans=="B":
                    print(A+" "+B+" "+C)
                elif ans=="C":
                    print(A+" "+C+" "+B)
                else:
                    print("wrong code")
        elif no==4:
            ans=input("All or Custom:")
            if ans=="All":
                print(A+" "+B+" "+C+" "+D)
            elif ans=="Custom":
                ans=input("A should be joined with:")
                if ans=="B":
                    print(A+" "+B+" "+C+" "+D)
                elif ans=="C":
                    print(A+" "+C+" "+B+" "+D)
                elif ans=="D":
                    print(A+" "+D+" "+B+" "+C)
                else:
                    print("wrong code")
    elif ans=="Replication":
        repno=int(input("Enter the no. of times it should be replicated:"))
        if no==2:
            print(A*repno,B*repno)
        elif no==3:
            print(A*repno,B*repno,C*repno)
        elif no==4:
            print(A*repno,B*repno,C*repno,D*repno)
        else:
            print(A*repno)
    else:
        print("wrong code")
else:
    if no==1:
        print(A)
    elif no>=2:
        print("Code for different operators:\n1 for addition\n2 for subtraction\n3 for multiplication\n4 for division\n5 for modulus\n6 for exponentiation\n")
        code = int(input("Enter the code:"))
        if code == 1:
            if no==2:
                print("result is",A+B)
            elif no==3:
                print("result is",A+B+C)
            else:
                print("result is",A+B+C+D)
        elif code == 2:
            if no==2:
                print("result is",A-B)
            elif no==3:
                print("result is",A-B-C)
            else:
                print("result is",A-B-C-D)
        elif code == 3:
            if no==2:
                print("result is",A*B)
            elif no==3:
                print("result is",A*B*C)
            else:
                print("result is",A*B*C*D)
        elif code == 4:
            if no==2:
                print("result is",A/B)
            elif no==3:
                print("result is",A/B/C)
            else:
                print("result is",A/B/C/D)
    elif code == 5:
        if no==2:
            print("result is",A%B)
        elif no==3:
            print("result is",A%B%C)
        else:
            print("result is",A%B%C%D)
    elif code == 6:
        if no==2:
            print("result is",A**B)
        elif no==3:
            print("result is",A**B**C)
        else:
            print("result is",A**B**C**D)
    else:
        print("No such code")

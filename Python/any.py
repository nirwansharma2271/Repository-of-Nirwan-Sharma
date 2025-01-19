import random
c=1
while c == 1:
    print("Code for the programs: \n pat for pattern program \n random for number generator \n eval for mathematical calculations infinity for infinite loop \n bigbrain for many mind breaking thoughts.")
    d=input("Choose one of the programs:")
    if d.lower() == "pat":
        a = input("Enter the text or number for a pattern:")
        b= a + " "
        i=int(input("Enter a number for the sequence:"))
        while i != 0:
            print(b * i)
            i= i - 1
    elif d.lower() == "exit":
        c=0
    elif d.lower() =="random":
        a=int(input("Lowest No.:"))
        b=int(input("Highest No.:"))
        number=random.choice(range(a,b))
        print(number,"\n")
    elif d.lower() == "eval":
        a=input("Enter the expression:")
        try:
            b= eval(a)
            print("Answer is ",b,"\n")
        except Exception as e:
            print("Error", "\n")
    elif d.lower() == "infinity":
        a =1
        while a == 1:
            print ("Infinite loop")
    elif d.lower() == "bigbrain":
        responses=random.choice(["When we yawn, deaf people think we are screaming.","If you are waiting for the waiter, then that makes you the waiter.","If you work as security at a samsung store, does that make you the guardian of the galaxy.","You have technically 2 minutes to live but everytime you breathe it resets.","Couldn't think of one."])
        print(responses,"\n")

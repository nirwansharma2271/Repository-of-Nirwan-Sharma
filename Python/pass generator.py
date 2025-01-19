import random
i=0
a=int(input("Enter Your Password Length:"))
char="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
passw=random.choice(char)
i+=1
t4='~`! @#$%^&*()-_+={}[]|\;:"<>,./?'
specchar=random.choice(t4)
ranchar=random.choice(char)
while i!=a-2:
    passw+=random.choice(char)
    i+=1
print("Password:",passw+specchar+ranchar)

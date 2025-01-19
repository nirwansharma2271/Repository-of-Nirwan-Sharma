# -*- coding: cp1252 -*-
import math
import random
"""#question 1
a=int(input("Enter the number:"))
if a==0 or a==1:
    print("Neither prime nor odd")

else:
    b=0
    for i in range(2,a):
        if a%i==0:
            b+=1
            break
        else:
            b+=0
    if b==1:
        print("it is not a prime no.")
    else:
        print("It is a prime no.")
#question 2
a=float(input("Enter your percentage:"))
if a>100:
    print("You're not a topper, You're dumb.")
elif a>=90 and a<100:
    print("Your grade is A.")
elif a>=80 and a<90:
    print("Your Grade is B.")
else:
    print("Your Grade is C.")
#question 3
a=int(input("Enter The Electricity Consumption:"))
if a>=100 and a<=200:
    b=a-100
    c=b*5
    print(c)
elif a>200:
    b=a-200
    c=b*10
    print(c+500)
else:
    print(0)
#question 4 (important)
print("Birth Number: A birth number is the single-digit total of your day number, i.e. the day on which you were born. For example, if your date of birth is 14, then your birth number is 1+4=5.\n Life Path Number: It is a single-digit total of your full date of birth. For example, your full date of birth is 14.4.2001, then by adding all the numbers in the date we get 3, so 3 is your life path number.")
a=input("Enter the birth-date in DD format:")
f=input("Enter the birth-date in DD MM YYYY format:")
b=a[0]
c=a[1]
try:
    d=int(b) + int(c)
    g=int(f[0])+int(f[1])+int(f[3])+int(f[4])+int(f[6])+int(f[7])+int(f[8])+int(f[9])
    h=str(g)
    i=int(h[0])+ int(h[1])
except Exception as e:
    print("You are Dumb")
if d==1 or d==10:
    print("It is the number of initiators. They can excel in their own independent career. They also have excellent leadership qualities. Best career options: CEO, Army Officer or commander, Political Leader, etc. If they want to opt for a job, it should be a leadership role.", "\n")
elif d==2 or d==11:
    print("Number 2 people are creative, charming, and soft-spoken. They do well in creative fields like a designer, artist, and creative writer. Being smart and soft-spoken, they can be good mediators, counselors, public relations officers, salespersons, etc. No. 2 people are also knowledge-oriented and can be great teachers, consultants, & diplomats.", "\n")
elif d==3:
    print(" Number 3 people are friendly, joyful, and helpful and are good at expressing themselves as well as entertaining others. The entertainment industry is the best option for them, be it acting, writing, singing, standup comedians, etc. They also have great leadership qualities, so they can opt for a political career, team leaders, army officers, commanders, etc. They can also be successful as Lawyers, Public Speakers, PRs, Teachers, Trainers, motivators, medicos etc.", "\n")
elif d==4:
    print("Number 4 people are multi-talented yet not money-minded. They can only make money through hard work. They are also critical thinkers so the best professions for them are journalism, lawyer, consultant, engineer, technologist, etc. They should avoid speculative professions like share market, gambling, etc.", "\n")
elif d==5:
    print(" Number 5 people are smart workers and also multi-talented. They can be successful in various fields. They can opt for careers in acting, music, journalism, law, film making, sales & marketing, public speaking, performing artists, detective agents, etc. These people are also natural gamblers and risk-takers and can make quick money in high-risk professions, however, there are chances of setbacks as well.", "\n")
elif d==6:
    print("Number 6 people are highly responsible and respected people. They are loving and caring towards their family, friends, and society at large. family-oriented, creative, cool, harmonious, humanitarian, and angels for their friends and related people. Also, creative, calm, and people’s person, should opt for creative professions like an architect, fashion designer, interior designer, healer, doctor, marketing & public relations, consultant, etc. They do also well in food-related businesses like restaurants, food processing, agriculture, and food products etc.", "\n")
elif d==7:
    print(" Number 7 people are introverts, spiritual, serious, and hard working. They can keep secrets and are great observers, thinkers, and analyzers. They can go in for professions like a spy, researcher, innovator, writer, teacher, trainer, and any profession related to occult sciences, religion, and spirituality. They also have a good voice, so they can become singers, voice artists, RJs, etc", "\n")
elif d==8:
    print("It is the number associated with money, wealth, power, administration and management. Number 8 people can opt for careers in finance, administrative services, banking and investment, NGOs, real estate and construction, etc. They can also be successful as politicians & organizational leaders.", "\n")
elif d==9:
    print("Number 9 people are humanitarians and great warriors. They should opt for a humanitarian profession or join the army, navy, air force, or police services. They can also become a successful sportsperson, especially the sports where high energy and stamina are required. Moreover, they can become very successful in real estate and construction business, Mining, and can create big industries and business houses.", "\n")
else:
    print("You are dumb.", "\n")
if i==1:
    print("It is the number of initiators. They can excel in their own independent career. They also have excellent leadership qualities. Best career options: CEO, Army Officer or commander, Political Leader, etc. If they want to opt for a job, it should be a leadership role.")
elif i==2:
    print("Number 2 people are creative, charming, and soft-spoken. They do well in creative fields like a designer, artist, and creative writer. Being smart and soft-spoken, they can be good mediators, counselors, public relations officers, salespersons, etc. No. 2 people are also knowledge-oriented and can be great teachers, consultants, & diplomats.")
elif i==3:
    print(" Number 3 people are friendly, joyful, and helpful and are good at expressing themselves as well as entertaining others. The entertainment industry is the best option for them, be it acting, writing, singing, standup comedians, etc. They also have great leadership qualities, so they can opt for a political career, team leaders, army officers, commanders, etc. They can also be successful as Lawyers, Public Speakers, PRs, Teachers, Trainers, motivators, medicos etc.")
elif i==4:
    print("Number 4 people are multi-talented yet not money-minded. They can only make money through hard work. They are also critical thinkers so the best professions for them are journalism, lawyer, consultant, engineer, technologist, etc. They should avoid speculative professions like share market, gambling, etc.")
elif i==5:
    print(" Number 5 people are smart workers and also multi-talented. They can be successful in various fields. They can opt for careers in acting, music, journalism, law, film making, sales & marketing, public speaking, performing artists, detective agents, etc. These people are also natural gamblers and risk-takers and can make quick money in high-risk professions, however, there are chances of setbacks as well.")
elif i==6:
    print("Number 6 people are highly responsible and respected people. They are loving and caring towards their family, friends, and society at large. family-oriented, creative, cool, harmonious, humanitarian, and angels for their friends and related people. Also, creative, calm, and people’s person, should opt for creative professions like an architect, fashion designer, interior designer, healer, doctor, marketing & public relations, consultant, etc. They do also well in food-related businesses like restaurants, food processing, agriculture, and food products etc.")
elif i==7:
    print(" Number 7 people are introverts, spiritual, serious, and hard working. They can keep secrets and are great observers, thinkers, and analyzers. They can go in for professions like a spy, researcher, innovator, writer, teacher, trainer, and any profession related to occult sciences, religion, and spirituality. They also have a good voice, so they can become singers, voice artists, RJs, etc")
elif i==8:
    print("It is the number associated with money, wealth, power, administration and management. Number 8 people can opt for careers in finance, administrative services, banking and investment, NGOs, real estate and construction, etc. They can also be successful as politicians & organizational leaders.")
elif i==9:
    print("Number 9 people are humanitarians and great warriors. They should opt for a humanitarian profession or join the army, navy, air force, or police services. They can also become a successful sportsperson, especially the sports where high energy and stamina are required. Moreover, they can become very successful in real estate and construction business, Mining, and can create big industries and business houses.")
else:
    print("You are dumb.")
# question 5
a=int(input("Enter a number:"))
if a%2==0:
    print("It is even")
else:
    print("It is odd")
# question 6
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>=b and b<=c:
    print(b,"is the smallest.")
elif a<=b and a<=c:
    print(a,"is the smallest.")
elif c<=a and c<=b:
    print(c,"is the smallest.")
# question 7
a=int(input("Enter the year:"))
if a%4==0:
    print("Leap year.")
else:
    print("Not a leap year.")
# question 8
a=int(input("Enter the number:"))
if a<0:
    print("It is negative.")
elif a>0:
    print("It is positive.")
else:
    print("The number is zero.")
# question 9
a=float(input("Enter your principle:"))
b=float(input("Enter your time:"))
c=float(input("Enter your rate:"))
si=(a*b*c)/100
asi=a+si
aci=a*(1+c/100)**b
ci=aci-a
print("If simple interest is applied: \n","SI:",si,"Amount:",asi)
print("If compound interest is applied: \n","CI:",ci,"Amount:",aci)
# question 10
a=float(input("Enter the first side:"))
b=float(input("Enter the second side:"))
c=float(input("Enter the third side:"))
s=(a+b+c)/2
hf=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of the triangle is:",hf)
# question 11
a=int(input("Enter the age:"))
b=int(input("Enter your height in centimeter:"))
if a>=18:
    if b>=150:
        print("You are eligbile for riding the roller coaster.")
    else:
        print("You are dwarf.")
else:
    print("You are a baby.")
# question 12
for i in range(1200,2200):
    if i%7==0:
        if i%5==0:
            print(i)
# question 13
a=int(input("Enter your age:"))
b=float(input("Enter you annual income in lakhs:"))
c=b*100000
if a>=40 and a<60:
    if c<300000:
        print("No tax will be applied.")
    elif c>=300000 and c<500000:
        d=c*0.05
        e=c-d
        print("Tax:",d,"Total amount left:",e)
    elif c>=500000 and c<1000000:
        d=c*0.2
        e=c-d
        print("Tax:",d,"Total amount left:",e)
    else:
        d=c*0.3
        e=c-d
        print("Tax:",d,"Total amount left:",e)
else:
    print("no tax")
# question 14
a=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
c=int(input("Enter the height:"))
sa=2*(a*b+b*c+c*a)
vol=a*b*c
print("The volume and surface area is:",sa,"and",vol,"Respectively.")"""
# question 15
a=float(input("Enter the height in centimetres:"))
feet=a//30.48
inchf=feet*12
inchi=a/2.54
inch=inchi-inchf
print("You are",int(feet),"feet","and",int(inch),"inch tall.")
"""# question 16
a=int(input("Enter the number:"))
if a<0:
    if a%2==0:
        print("It is a negative and even number.")
    else:
        print("It is a negative and odd number.")
elif a>0:
    if a%2==0:
        print("It is a positive and even number.")
    else:
        print("It is a positive and odd number.")
else:
    print("It is zero.")
# question 17
a=int(input("Enter temperature for day 1:"))
b=int(input("Enter temperature for day 2:"))
c=int(input("Enter temperature for day 3:"))
d=int(input("Enter temperature for day 4:"))
e=int(input("Enter temperature for day 5:"))
f=int(input("Enter temperature for day 6:"))
g=int(input("Enter temperature for day 7:"))
avg=(a+b+c+d+e+f+g)/7
print("Average temperature for this week:",avg)
# question 18 (important)
i=0
j=0
while i<5 or j<5:
        com=random.choice(["rock","paper","scissors"])
        a=input("Enter your choice(Rock/paper/scissors):")
        if a.lower()=="scissors":
                if com=="scissors":
                        print("Tie.")
                        
                elif com=="paper":
                        print("You won, my choice was",com)
                        i+=1
                        
                else:
                        print("I won, my choice was",com)
                        j+=1
                        
        elif a.lower()=="rock":
                if com=="rock":
                        print("Tie.")
                        
                elif com=="scissors":
                        print("You won, my choice was",com)
                        i+=1
                        
                else:
                        print("I won, my choice was",com)
                        j+=1
                        
        elif a.lower()=="paper":
                if com=="paper":
                        print("Tie.")
                        
                elif com=="rock":
                        print("You won, my choice was",com)
                        i+=1
                        
                else:
                        print("I won, my choice was",com)
                        j+=1
                        
        else:
                print("WHAT DA HAIL!!!!")
                break
        if i>5 or j>5:
                break
if j>5:
        print("I won.")
        print(i,j)
        
elif i>5:
        print("You won")
        print(i,j)
else:
        print("No one won.")
# question 19"""
"""a=int(input("Enter the number of days:"))
if a>0 and a<=5:
        b=a*10
        print("Total amount:",b)
elif a>5 and a<=10:
        b=(a-5)*20
        print("Total amount:",b+50)
elif a>10:
        b=(a-10)*30
        print("Total amount:",b+150)
else:
        print("There is an error in your input.")
# question 20
a=int(input("Enter a number(UPTO 1000):"))
if a>0 and a<10:
        print(a,"is the last digit of your no.")
elif a>9 and a<100:
        b=a%10
        c=a//10
        print(c,"is the first digit of your no.\n",b,"is the last digit of your no.\n")
elif a>99 and a<1000:
        b=a%100
        c=a//100
        d=b%10
        e=b//10
        print(c,"is the first digit of your no.\n",d,"is the middle digit of your no.\n",e,"is the last digit of your no.\n")
elif a==1000:
          print("1 is the first digit of your no.\n","0 is the middle digit of your no.\n","0 is the middle digit of your no.\n","0 is the last digit of your no.\n")
else:
        print("ERROR")
# question 21
a=int(input("Enter a number:"))
b=str(a)[::-1]
c=int(b)
if a==c:
        print("It is a palindrome.")
else:
        print("Not a palindrome.")
# question 22
a=int(input("Till what should we do fizzbuzz?:"))
for i in range(1,a):
        if i%5==0 and i%2==0:
                print("FizzBuzz")
        elif i%2==0:
                print("Buzz")
        elif i%5==0:
                print("Fizz")
        else:
                print(i)"""


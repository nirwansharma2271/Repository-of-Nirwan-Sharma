# -*- coding: cp1252 -*-
name=input("What's Your Name?:")
ques=[
    ("What is the capital of Belarus?:","A]Keiv","B]Minsk","C]Helsinki","D]Gibraltar","B"),
    ("Which of these Games is about to have a new sequel coming up in 2025?:","A]GTA","B]Minecraft","C]Fall Guys","D]Among us","A"),
    ("When the First Battle of Panipat took place?:","A]1527","B]1724","C]1526","D]1428","C"),
    ("Which Youtuber has started a Prime Video Series having a contest of cash price as 5 million dollars?","A]Jimmy Donaldson","B]Felix Arvid Ulf Kjellberg","C]Eva Diana Kidisyuk","D]Vashketov brothers","A"),
    ("Who gave an uncertainty principle, a leading theory in quantum mechanics?","A]Erwin Schrodinger","B]Max Planck","C]Niels Bohr","D]Werner Heisenberg","D")
    ]
print("Hello",name+"!", "Welcome To an MCQ based quiz by Nirwan Sharma of 9th D.")
print("RULES:-\n\
      *This quiz contain 5 itions with 4 options and only one correct answer.\n\
      *The itions will be asked from the following topics:Capitals of countries, Popular video games, Historical events, Famous personalities, and General science.\n\
      *You'll get 1 points on one correct ition and -1 as a penalty for incorrect answer.\n\
      *Don't Cheat.")
confirm=input("Are you ready?(yes/no):")
if confirm.lower()=="yes":
    a=0
    b=0
    c=0
    for i in ques:
        print(i[0])
        print(i[1],i[2],i[3],i[4],sep="\n")
        ans=input("ANSWER(A/B/C/D):")
        if ans.upper()==i[5]:
            print("CORRECT!")
            a+=1
            b+=1
        else:
            print("WRONG!")
            a-=1
            c+=1
    print("Name:",name)
    print("Total Score:",str(a)+"/5","with",b,"correct and",c,"incorrect answers")


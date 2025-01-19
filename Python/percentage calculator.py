print("Only use if you have got the marks of PA 1 and PA 2.")
rsvp=input("Have you got marks for Half Yearly?(Y/N):")
rsvp1=input("Have you got marks for PA 3?(Y/N):")
rsvp2=input("Have you got marks for Annual exam?(Y/N):")
if rsvp.lower()=="y" and rsvp1.lower()=="y" and rsvp2.lower()=="y":
    a=int(input("Enter the marks of Maths (Best PA):"))
    b=int(input("Enter the marks of English (Best PA):"))
    c=int(input("Enter the marks of Hindi (Best PA):"))
    d=int(input("Enter the marks of SST (Best PA):"))
    e=int(input("Enter the marks of Science (Best PA):"))
    f=int(input("Enter the marks of Computer (VIVA):"))
    a1=int(input("Enter the marks of Maths (Half yearly):"))
    b1=int(input("Enter the marks of English (Half yearly):"))
    c1=int(input("Enter the marks of Hindi (Half yearly):"))
    d1=int(input("Enter the marks of SST (Half yearly):"))
    e1=int(input("Enter the marks of Science (Half yearly):"))
    f1=int(input("Enter the marks of Computer (Half yearly):"))
    a3=int(input("Enter the marks of Maths (PA 3):"))
    b3=int(input("Enter the marks of English (PA 3):"))
    c3=int(input("Enter the marks of Hindi (PA 3):"))
    d3=int(input("Enter the marks of SST (PA 3):"))
    e3=int(input("Enter the marks of Science (PA 3):"))
    f3=int(input("Enter the marks of Computer (VIVA):"))
    a2=int(input("Enter the marks of Maths (Annual Exam):"))
    b2=int(input("Enter the marks of English (Annual Exam):"))
    c2=int(input("Enter the marks of Hindi (Annual Exam):"))
    d2=int(input("Enter the marks of SST (Annual Exam):"))
    e2=int(input("Enter the marks of Science (Annual Exam):"))
    f2=int(input("Enter the marks of Computer (Annual Exam):"))
    ta=a+a1
    tb=b+b1
    tc=c+c1
    td=d+d1
    te=e+e1
    tf=f+f1
    phalf=(ta+tb+tc+td+te+tf)/6
    ta1=a3+a2
    tb1=b3+b2
    tc1=c3+c2
    td1=d3+d2
    te1=e3+e2
    tf1=f3+f2
    taf=(ta1/2) + (ta/2)
    tbf=(tb1/2) + (tb/2)
    tcf=(tc1/2) + (tc/2)
    tdf=(td1/2) + (td/2)
    tef=(te1/2) + (te/2)
    tff=(tf1/2) + (tf/2)
    pfinal=(taf+tbf+tcf+tdf+tef+tff)/6
    print("Student Report(Half Yearly)")
    print("Maths:",ta)
    print("English:",tb)
    print("Hindi:",tc)
    print("SST:",td)
    print("Science:",te)
    print("Computer:",tf)
    print("Percentage:",phalf,"%")
    print("Student Report(Final Exam)")
    print("Maths:",taf)
    print("English:",tbf)
    print("Hindi:",tcf)
    print("SST:",tdf)
    print("Science:",tef)
    print("Computer:",tff)
    print("Percentage:",pfinal,"%")
elif rsvp.lower()=="n":
    a=int(input("Enter the marks of Maths (Best PA):"))
    b=int(input("Enter the marks of English (Best PA):"))
    c=int(input("Enter the marks of Hindi (Best PA):"))
    d=int(input("Enter the marks of SST (Best PA):"))
    e=int(input("Enter the marks of Science (Best PA):"))
    p=(a+b+c+d+e)
    print("Student Report(BEST PA)")
    print("Maths:",a)
    print("English:",b)
    print("Hindi:",c)
    print("SST:",d)
    print("Science:",e)
    print("Percentage:",p,"%")
elif rsvp1.lower()=="n":
    a=int(input("Enter the marks of Maths (Best PA):"))
    b=int(input("Enter the marks of English (Best PA):"))
    c=int(input("Enter the marks of Hindi (Best PA):"))
    d=int(input("Enter the marks of SST (Best PA):"))
    e=int(input("Enter the marks of Science (Best PA):"))
    f=int(input("Enter the marks of Computer (VIVA):"))
    a1=int(input("Enter the marks of Maths (Half yearly):"))
    b1=int(input("Enter the marks of English (Half yearly):"))
    c1=int(input("Enter the marks of Hindi (Half yearly):"))
    d1=int(input("Enter the marks of SST (Half yearly):"))
    e1=int(input("Enter the marks of Science (Half yearly):"))
    f1=int(input("Enter the marks of Computer (Half yearly):"))
    ta=a+a1
    tb=b+b1
    tc=c+c1
    td=d+d1
    te=e+e1
    tf=f+f1
    phalf=(ta+tb+tc+td+te+tf)/6
    print("Student Report(Half Yearly)")
    print("Maths:",ta)
    print("English:",tb)
    print("Hindi:",tc)
    print("SST:",td)
    print("Science:",te)
    print("Computer:",tf)
    print("Percentage:",phalf,"%")
elif rsvp2.lower()=="n":
    a=int(input("Enter the marks of Maths (Best PA):"))
    b=int(input("Enter the marks of English (Best PA):"))
    c=int(input("Enter the marks of Hindi (Best PA):"))
    d=int(input("Enter the marks of SST (Best PA):"))
    e=int(input("Enter the marks of Science (Best PA):"))
    f=int(input("Enter the marks of Computer (VIVA):"))
    a1=int(input("Enter the marks of Maths (Half yearly):"))
    b1=int(input("Enter the marks of English (Half yearly):"))
    c1=int(input("Enter the marks of Hindi (Half yearly):"))
    d1=int(input("Enter the marks of SST (Half yearly):"))
    e1=int(input("Enter the marks of Science (Half yearly):"))
    f1=int(input("Enter the marks of Computer (Half yearly):"))
    a3=int(input("Enter the marks of Maths (PA 3):"))
    b3=int(input("Enter the marks of English (PA 3):"))
    c3=int(input("Enter the marks of Hindi (PA 3):"))
    d3=int(input("Enter the marks of SST (PA 3):"))
    e3=int(input("Enter the marks of Science (PA 3):"))
    ta=a+a1
    tb=b+b1
    tc=c+c1
    td=d+d1
    te=e+e1
    tf=f+f1
    phalf=(ta+tb+tc+td+te+tf)/6
    print("Student Report(Half Yearly)")
    print("Maths:",ta)
    print("English:",tb)
    print("Hindi:",tc)
    print("SST:",td)
    print("Science:",te)
    print("Computer:",tf)
    print("Percentage:",phalf,"%")
    p=(a3+b3+c3+d3+e3)
    print("Student Report(PA 3)")
    print("Maths:",a3)
    print("English:",b3)
    print("Hindi:",c3)
    print("SST:",d3)
    print("Science:",e3)
    print("Percentage:",p,"%")
else:
    print("ERROR")

print("You are NINO.")
print("Birth Number: A birth number is the single-digit total of your day number, i.e. the day on which you were born. For example, if your date of birth is 14, then your birth number is 1+4=5.\n Life Path Number: It is a single-digit total of your full date of birth. For example, your full date of birth is 14.4.2001, then by adding all the numbers in the date we get 3, so 3 is your life path number.")
a=input("Enter the birth-date in DD format:")
f=input("Enter the birth-date in DD MM YYYY format:")
b=a[0]
c=a[1]
d=int(b) + int(c)
g=int(f[0])+int(f[1])+int(f[3])+int(f[4])+int(f[6])+int(f[7])+int(f[8])+int(f[9])
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
if g>9:
    h=str(g)
    i=int(h[0])+ int(h[1])
    if i>9:
        j=str(i)
        k=int(j[0]) + int(j[1])
        i=k
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
    elif i==9
        print("Number 9 people are humanitarians and great warriors. They should opt for a humanitarian profession or join the army, navy, air force, or police services. They can also become a successful sportsperson, especially the sports where high energy and stamina are required. Moreover, they can become very successful in real estate and construction business, Mining, and can create big industries and business houses.")
    else:
        print("You are NINO.")
else:
    if g==1:
        print("It is the number of initiators. They can excel in their own independent career. They also have excellent leadership qualities. Best career options: CEO, Army Officer or commander, Political Leader, etc. If they want to opt for a job, it should be a leadership role.")
    elif g==2:
        print("Number 2 people are creative, charming, and soft-spoken. They do well in creative fields like a designer, artist, and creative writer. Being smart and soft-spoken, they can be good mediators, counselors, public relations officers, salespersons, etc. No. 2 people are also knowledge-oriented and can be great teachers, consultants, & diplomats.")
    elif g==3:
        print(" Number 3 people are friendly, joyful, and helpful and are good at expressing themselves as well as entertaining others. The entertainment industry is the best option for them, be it acting, writing, singing, standup comedians, etc. They also have great leadership qualities, so they can opt for a political career, team leaders, army officers, commanders, etc. They can also be successful as Lawyers, Public Speakers, PRs, Teachers, Trainers, motivators, medicos etc.")
    elif g==4:
        print("Number 4 people are multi-talented yet not money-minded. They can only make money through hard work. They are also critical thinkers so the best professions for them are journalism, lawyer, consultant, engineer, technologist, etc. They should avoid speculative professions like share market, gambling, etc.")
    elif g==5:
        print(" Number 5 people are smart workers and also multi-talented. They can be successful in various fields. They can opt for careers in acting, music, journalism, law, film making, sales & marketing, public speaking, performing artists, detective agents, etc. These people are also natural gamblers and risk-takers and can make quick money in high-risk professions, however, there are chances of setbacks as well.")
    elif g==6:
        print("Number 6 people are highly responsible and respected people. They are loving and caring towards their family, friends, and society at large. family-oriented, creative, cool, harmonious, humanitarian, and angels for their friends and related people. Also, creative, calm, and people’s person, should opt for creative professions like an architect, fashion designer, interior designer, healer, doctor, marketing & public relations, consultant, etc. They do also well in food-related businesses like restaurants, food processing, agriculture, and food products etc.")
    elif g==7:
        print(" Number 7 people are introverts, spiritual, serious, and hard working. They can keep secrets and are great observers, thinkers, and analyzers. They can go in for professions like a spy, researcher, innovator, writer, teacher, trainer, and any profession related to occult sciences, religion, and spirituality. They also have a good voice, so they can become singers, voice artists, RJs, etc")
    elif g==8:
        print("It is the number associated with money, wealth, power, administration and management. Number 8 people can opt for careers in finance, administrative services, banking and investment, NGOs, real estate and construction, etc. They can also be successful as politicians & organizational leaders.")
    elif g==9:
        print("Number 9 people are humanitarians and great warriors. They should opt for a humanitarian profession or join the army, navy, air force, or police services. They can also become a successful sportsperson, especially the sports where high energy and stamina are required. Moreover, they can become very successful in real estate and construction business, Mining, and can create big industries and business houses.")
    else:
        print("You are dumb.")


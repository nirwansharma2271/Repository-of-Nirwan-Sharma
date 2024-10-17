print("Zeller's Algorithm")
bd = input("Enter the date in DD MM YYYY format: ")
lbd = bd.split()
d = int(lbd[0])
m = int(lbd[1])
y = int(lbd[2])
if m == 1 or m == 2:
    m = m + 12
    y = y - 1
k = y % 100  
j = y // 100 
h = (d + ((26 * (m + 1)) // 10) + k + (k // 4) + (j // 4) + (5 * j)) % 7
if h == 0:
    print("Saturday")
    print("Saturday's child works hard for a living")
elif h == 1:
    print("Sunday")
    print("the child born on the Sabbath Day,Is fair and wise and good in every way")
elif h == 2:
    print("Monday")
    print("Monday's child is fair of face")
elif h == 3:
    print("Tuesday")
    print("Tuesday's child is full of grace")
elif h == 4:
    print("Wednesday")
    print("Wednesday's child is full of woe")
elif h == 5:
    print("Thursday")
    print("Thursday's child has far to go")
elif h == 6:
    print("Friday")
else:
    print("ERROR")


n = 1042000
e = 702648265

for i in range(n,e+1):
    t=i
    sum = 0
    order = len(str(i))
    com = i
    while (t>0):
        number = t%10
        sum += number**order
        t = t//10

    if (sum == com):
        print(f"{com} is a armstrong number")
        break

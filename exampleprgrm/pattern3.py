lmt=int(input("enter a limit"))
lmt1=5
for i in range(1,lmt+1):
    for j in range(0,lmt1*2):
        print("*",end=" ")
    print()
    lmt1=lmt1-1
    for k in range(1,i+1):
        print("*")


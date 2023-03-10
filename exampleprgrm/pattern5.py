lmt=int(input("enter limit"))
sp=2
for i in range(1,lmt+1):
    for j in range(1,sp+1):
        for k in range(1,lmt):
            print("*",end=" ")
        print()
    for h in range(1,i*lmt+3):
        print("*",end=" ")
    print()

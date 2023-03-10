lmt=int(input("enter a limit"))
for i in range(1,lmt+1):
    for j in range(1,i*lmt+1):
        print("*",end=" ")
    print()
    for k in range(1,i*lmt+1):
        if i != 3:
            print("*")

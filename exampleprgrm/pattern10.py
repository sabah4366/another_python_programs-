
lmt=int(input("enter a limit"))
for i in range(0,lmt+1):
    for j in range(1,lmt+1-i):
        print(end=" ")
    for k in range(0,i):
        print(chr(65+k) ,end="")
    print()

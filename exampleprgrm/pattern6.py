limit=int(input("enter limit"))
print("*")
for i in range(1,limit+1):
    for j in range(1,i+1):
        for k in range(1,i+1):
            print("*",end="")
        print()
    for h in range(1,i*limit+1):
        print("*",end="")
    print()
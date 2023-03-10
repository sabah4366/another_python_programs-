num=int(input("enter a limit"))
limit=5
for i in range(1,num+1):
    for j in range(1,i*num*2):
        print("*",end=" ")
    print()
    for k in range(1,i*num+1):
        if i != 3:
            print("*")






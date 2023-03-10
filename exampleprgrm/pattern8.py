#pyramid
lmt=int(input("enter limit"))
var=1
for i in range(1,lmt+1):
    for j in range(1,lmt+1-i):
        print(end=" ")
    for k in range(1,var+1):
        print("*",end="")
    var+=2
    print()




# reverse pyramid
lmt=int(input("enter limit"))
var=9
for i in range(1,lmt+1):
    for k in range(1, i):
        print(end=" ")
    for j in range(1,var+1):
        print("*",end="")
    print()
    var-=2


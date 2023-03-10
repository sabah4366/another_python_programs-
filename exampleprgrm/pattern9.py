#diamond printing
lmt=int(input("enter limit"))
var=1
sp=5
for i in range(1,2*lmt+1):
    for j in range(1,sp):
        print(end=" ")
    for k in range(1,var+1):
        print("*",end="")
    if i>=lmt:
        var -= 2
        sp+=1
    else:
        var += 2
        sp-=1
    print()




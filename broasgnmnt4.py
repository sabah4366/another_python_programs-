#write a program of multiplcation of a given number,accept the number from user and ouput like 1*5=5
limit=int(input("enter a limit"))
num=int(input("enter a number"))
for i in range(1,limit+1,1):
    print(i,"*",num,"=",i*num)




#program-2 :find the sum of odd numbers for a given limit,accept a limit from the user

n=int(input("enter a limit"))
sum=0
print("odd numbers are")
for s in range(1,n,2):
    print(s)
    sum=sum+s
print("total sum of odd number is ",sum)





'''program-1 :-write a program to print the following pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
num=int(input("enter the limit"))
for i in range(1,num+1,1):
    print(end="\n")
    for j in range(1,i+1,1):
        print(j ,end=" ")


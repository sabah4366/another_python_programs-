#prime
# num1=int(input("enter a number"))
# count=0
# for i in range(2,num1):
#     if num1%i==0:
#         count+=1
# if count==0:
#     print("prime")
# else:
#     print("not prime")


#count factors and print factors
# num1=int(input("enter a number"))
# c=0
# for i in range(1,num1+1):
#     if num1%i==0:
#         print(i)
#         c+=1
# print(c)

#fibanocci series
# num1=int(input("enter a number"))
# f=0
# s=1
# for i in range(num1+1):
#     print(f)
#     t=f+s
#     f=s
#     s=t

#count the vowels
# strng=input("enter a string")
# c=0
# for i in strng:
#     if i in "aeiouAEIOU":
#         c+=1
# print(c)


#sum of two numbers using lambda
# sum=lambda  x,y:x+y
# print(sum(3,4))
#


#greater than 3numbers
# num1=3
# num2=6
# num3=10
# result=lambda x,y,z:x if x>y and x>z else y if y>x and y>z else z
# print(result(num1,num2,num3))


#print last digit
# num=1234
# last=num%10
# print(last)
#
# avoid last number
# num=1234
# last=num//10
# print(last)

#n+nn+nnn+nnnn
# num=5
# sum=0
# t=num
# for i in range(1,num):
#     print(num,end="")
#     if i<t-1:
#         print('+',end="")
#     else:
#         print("=",end="")
#     sum += num
#     num=num*10+t
# print(sum)



#amstrong
# amst=int(input("enter a number"))
# num2=amst
# c=len(str(amst))
# sum=0
# for i in range(amst):
#     num1=num2%10
#     sum=sum+num1**c
#     num2=num2//10
# print(sum)
# if sum==amst:
#     print("amstrong ")
#
# else:
#     print("not amstrong")


#sort
lst=[7,6,3,9,4,0,5]
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            t=lst[i]
            lst[i]=lst[j]
            lst[j]=t
print(lst)

lmt=5
sp=lmt
for i in range(lmt,0,-1):
    for j in range(i,lmt):
        print('',end=" ")
    for k in range(i):
        print("*",end=" ")
    print()


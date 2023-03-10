#
# #1
# num=28
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum=sum+i
# if sum==num:
#     print("it is a perfect number")
# else:
#     print("not perfect number")
#
# #2
# lmt=5
# for i in range(lmt+1):
#     for j in range(0,i):
#         print(" ",end="")
#     for k in range(lmt+1):
#         print("*",end=" ")
#     lmt=lmt-1
#     print()
#
#
#
# #3
# lmt=5
# for i in range(1,lmt+1):
#     for j in range(1,i+1):
#         print(chr(i+64),end=" ")
#     print()
#
#
# #4
# strng="the struggle will create a sucesfull life".split()
# newlst=[i for i in strng if len(i)%2==0]
# print(newlst)
#
# #5
# ln=4
# lst=['sabah','sani','sala','saleem','fyha','faizasaleem','shiyas']
# newlst=[x for x in lst if len(x)>ln]
# print(newlst)
#
#
# #6
# strng=input("enter a string")
# if len(strng)%2==0:
#     st1=strng[:int(len(strng)//2)]
#     st2=strng[int(len(strng)//2):]
# else:
#     st1=strng[:int(len(strng)//2)]
#     st2=strng[(int(len(strng)//2)+1):]
# if st1==st2:
#     print("symmetric")
# else:
#     print("not symmetric")
#
#
# #7
# strng="hai sabah how are you"
# newst=[i for i in strng if strng.index(i)%2==0]
# print(newst)
#
#
#
# #8
# strng=input("enter a sentence").split()
# count=0
# for i in strng:
#     count=count+1
# print(count)

#9



year=int(input("enter year"))
if year%400==0 or year%100!=0 and year%4==0:
    print("it is a leap year")
else:
    print("it is not a leap year")

# # #10
# lst=[1,3,5,6,8]
# lst1=list(map(lambda x:x*x,lst))
# print(lst1)
#
# # 11
# lis=input("enter a list").split()
# list1=list(map(int,lis))
# ln=len(list1)
# for i in range(0,ln):
#     for j in range(i,ln):
#         if list1[i]>list1[j]:
#             t=list1[i]
#             list1[i]=list1[j]
#             list1[j]=t
# # print(list1)
# #
# # #12
# lst=input("enter a numbers").split()
# nwlst=list(map(int,lst))
# gn=10
# print(nwlst)
# nws=[i for i in nwlst if i>gn]
# print(nws)
#
#
# #13
# strng="HAI SABAH how are YOu"
# upp=0
# low=0
# for i in strng:
#     if i.isupper():
#         upp=upp+1
#     elif i.islower():
#         low=low+1
# print(f"count of uppercase letters are{upp}\ncount of lower case letters are{low}")
#
#
#
# #14
# farm={1:'Eeman',2:'Catrine',3:'David'}
# farm[8]='jack'
# print(len(farm))
# farm.pop(2)
# print(farm)
#
#
#
# #15
# tpl=(input("enter numbers")).split()
# nwtpl=tuple(map(int,tpl))
# print(nwtpl)
# newtpl1=tuple(i for i in nwtpl if i%3==0)
# print(newtpl1)
#

# import array as arr
# #1
# str=input("enter a char input")
# print(str)
#
# #2
# num1=int(input("enter two numbers"))
# num2=float(input())
# sum=num1+num2
# print('sum is:',float(sum))
#
# #3
# P=int(input("enter three numbers"))
# R=float(input())
# n=float(input())
# SI=(P*R*n)/100
# print("simple interst is:",float(SI))
#
#
# #4
# mark=float(input("enter your mark "))
# if mark>50 and mark<=100:
#     print("Passed")
# else:
#     print("Failed")
#
#
# #5
# totalmark=float(input("enter the total mark perscentage"))
# if totalmark>=90 and totalmark<=100:
#     print("GRADE A")
# elif totalmark>=80 and totalmark<90:
#     print("GRADE B")
# elif totalmark>=70 and totalmark<80:
#     print("GRADE C")
# elif totalmark>=60 and totalmark<70:
#     print("GRADE D")
# elif totalmark>=50 and totalmark<60:
#     print("GRADE E")
# else:
#     print("FAILED")
#
#
# #6
#
print("1:SUNDAY \n2:MONDAY \n3:TUESDAY \n4:WEDNESDAY \n5:THURSDAY \n6:FRIDAY  \n7:SATURDAY")

choice=int(input("enter your choice"))
match choice:
    case 1:
        print("SUNDAY")
    case 2:
        print("MONDAY")
    case 3:
        print("TUESDAY")
    case 4:
        print("WEDNESDAY")
    case 5:
        print('THURSDAY')
    case 6:
        print("FRIDAY")
    case 7:
        print("SATURDAY")
    case wrong:
        print(f" {wrong} :is wrong choice")
#
# #7
# mul=int(input("enter a number"))
# for i in range(1,11,1):
#     print(i,"*",mul,"=",i*mul)
#
# #8
# lmt=int(input("enter a limit"))
# sum=0
# for i in range(lmt):
#     if i%2!=0:
#         sum=sum+i
#
# print("sum of odd numbers within a limit=",sum)
#
# #9
# lmt=int(input("enter a limit"))
# for i in range(lmt+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
#
#
# #10
#
# lmt=int(input("enter the limit of an array"))
# print("enter the values of first array")
# arry1=arr.array('i',[])
# arry2=arr.array('i',[])
# arry3=arr.array('i',[])
# for i in range(lmt):
#     x=int(input())
#     arry1.append(x)
#
# print("enter the values of second  array")
# for j in range(lmt):
#     y=int(input())
#     arry2.append(y)
# arry1,arry2=arry2,arry1
# print("first array is",arry1)
# print("second array is",arry2)
#
#
# #11
#
# lmt=int(input("enter the array limit"))
# print("enter the array values")
# array1=arr.array('i',[])
# c=0
# for i in range(lmt):
#     val=int(input())
#     array1.append(val)
# for i in array1:
#     if i%2==0:
#         c+=1
# print(f"the count of the even numbers in this array={c}")
#
# #12
# arry=arr.array('i',[])
# lmt=int(input("enter the lmt of n array "))
# print("enter the values of an array")
# for i in range(lmt):
#     val=int(input())
#     arry.append(val)
# for i in range(lmt):
#     for j in range(i+1,lmt):
#         if arry[i]>arry[j]:
#             temp=arry[i]
#             arry[i]=arry[j]
#             arry[j]=temp
# print(arry)
#

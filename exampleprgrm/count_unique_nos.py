#1

lmt=int(input("enter the limit of the list"))
lst=[]
for i in range(lmt):
    values=int(input("=>"))
    lst.append(values)
print(lst)
lst1=[]
count=0
for i in lst:
    if i not in lst1:
        count = count + 1
        lst1.append(i)
print(count)

#2
lmt=int(input("enter the limit of the list"))
lst=[]
for i in range(lmt):
    values=int(input("=>"))
    lst.append(values)
print(lst)
lst[0],lst[-1]=lst[-1],lst[0]
print(lst)

#3
lst=[1,2,3,4]
print(lst)
pos1,pos2=1,3
lst[pos1],lst[pos2]=lst[pos2],lst[pos1]
print(lst)


#4
a=9
b=5
if a>b:
    print(a)
else:
    print(b)
#4 th using ternary operator

print(a if a>b else b)

#4th using lambda function
ma=(lambda a,b:a if a>b else b)
print(ma(a,b))
#or using list comprehension
lst=[a if a>b else b]
print(lst)


#5
lst=[1,2,3,4,5,6,7,8]
if 8 in lst:
    print("existt")
else:
    print("not exist")

#5th using list comprehension
lst1=['exist' if 6 in lst else 'not exist']
print(lst1)

#5th using lambda
lst2=(lambda x:'exist ' if x in lst else 'not exist')
print(lst2(10))

import list_programs.count_unique_nos

#6
lst=[1,2,3,4,5,6,1,9,1]
x=1
count=0
for i in lst:
    if i==x:
        count=count+1
print(count)


#6th using count method
print(lst.count(x))


#7
lst=[1,2,3,4,-1,-4,-6,1,5]
count,sum,co,summ=0,0,0,0
for i in lst:
    if i>0:
        count=count+1
        sum=sum+i
    else:
        co=co+1
        summ+=i
print("positive numbers {}\nnegative numbers{}\nsum of positive numbers{}\nsum of negative{}".format(count,co,sum,summ))


#8
lst=[1,3,2,4,6,7]
# lst.remove(2)
# lst.remove(3)
# print(lst)

#8 using another method
lst=[1,2,3,4,5,6,7,8,9]
for i in lst:
    if i%2==0:
        lst.remove(i)
print(lst)

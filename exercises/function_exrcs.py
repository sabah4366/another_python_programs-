'''
#find maximum of thre numbers
a=int(input("enter 3 numbers"))
b=int(input())
c=int(input())
def maxm(num1,num2,num3):
    if num1>num2 and num1>num3:
        print("maxm numbers is:",num1)
    elif num2>num1 and num2>num3:
        print("maxm numbers is:",num2)
    else:
        print("maxm numbers is:",num3)
maxm(a,b,c)




#2-sum of alll numbers in the list
def sum(values):
    sum=0
    for i in values:
        sum=sum+i
    print(sum)
listt=[8,2,3,0,7]
sum(listt)



#3-multiplication of all numbers in the list
list=[8,2,3,-1,7]

def mul(values):
    mul=1
    for i in values:
        mul*=i
    print(mul)
mul(list)



#4-reverse a string
str1=input("enter a string")
lenth=len(str1)
str2=''
while lenth>0:
    str2=str2+str1[lenth-1]
    lenth=lenth-1

print(str2)



#5 factorial of non integer mumber
n=int(input("enter a number"))

def fact(a):
    if a==0:
        return 1

    else:
        return a*fact(a-1)
fact(n)

#6number falls in a range
num=int(input("enter a number"))
def funct(a):
        if a in range(10):
            print("yes ")

        else:
            print("no")

funct(num)



#8-take a list and return a new list with unique elements of the first list
list1=[1,2,3,4,5,6,7,8,4,6,3]
list2=[]
def unq(lst):
    for i in list1:
        if i not in list2:
            list2.append(i)
    print(list2)
unq(list1)

#7-count of uppercase and lowercase letters in a given string
string1=input("enter a string")
def chck(str1):
    count = 0
    co = 0
    for i in str1:
        if i.isupper():
            count=count+1
        else:
            co=co+1
    print(f"uppercase letters {count}\nlowercase letters{co}")
chck(string1)


#9 number that is a prime number or not
n=int(input("enter a number"))
def prime(s):
    flag=0
    for i in range(2,s):
        if s%i==0:
            flag=1
            break
    if flag==0:
        print("it is prime")
    else:
        print("it is not prime")

prime(n)

#10-print even number in a list
a=[11,2,3,4,5,6,7,8,9]
def even(n):
    for i in a:
        if i%2==0:
            print(i)

even(a)



#12-check the string is palindrome or not
st=input("enter a string")
s=len(st)
def pal(a):
    flag=0
    for i in range(s):
        if st[i]!=st[s-1-i]:
            flag=1
            break
    if flag==1:
        print("it is not plaindromw")
    else:
        print("pal")

pal(st)


#16
lmt=[]
for i in range(1,31):
        lmt.append(i**2)
print(lmt)


#17
def fun(name,salary=12000):
        print(f"name:{name}  salary:{salary}")
fun("ben",9000)
fun("benny")



#18
def sum(a,b):
        def add(c,d):
                return c+d
        addd=add(a,b)
        return addd+12


print(sum(2,3))

#19
n=10
def rec(a):
        if a==0:
                return 0
        else:
                return a+rec(a-1)
s=rec(n)
print(s)
#one function to new function
def old_name(name,age):
        print(name,age)
new_name=old_name
old_name("sabah",12)

#even number list 0 to 30
print(list(range(4,30,2)))



#max number in a list
lst=[1,2,3,4,52,33,12,34]
print(max(lst))
'''

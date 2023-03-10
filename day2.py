'''#13  there are two model palindrome in python
#model-1
st=input("enter a string")
flag=0
sa=len(st)
for i in range(sa):
    if st[i]!=st[sa-i-1]:
        flag=1
        break
if flag==1:
    print("is not palindrome")
else:
    print("is palindrome")
#model-2
st=input("enter  a string")
ds=st[::-1]
if st==ds:
    print("is palindrome")
else:
    print("not palindrome")

#16
num=int(input("enter a number"))
flag=0
for i in range(2,num):
    if num%i==0:
        flag=1
        break
if flag==1:
    print(f"{num}: is not a prime number")
else:
    print(f"{num}: is a prime")


#15
def mainarray():
    a=[]
    getarray(a)
    diplayarray(a)


def getarray(s):
    len=int(input("enter the limit"))
    print("enter the values to the array")
    for i in range(len):
        val=int(input())
        s.append(val)

def diplayarray(s):
    print(s)

mainarray()


#21
array1=[]
array2=[]
lmt=int(input("enter limit"))
print("enter the values")
for i in range(lmt):
    array1.append(int(input("=>")))
for i in range(0,lmt-1):
    array2.append(array1[i]*array1[i+1])
print(array2)


#20
lmt=int(input("enter a limit"))
star=1
for i in range(lmt):
    for j in range(i+1):
        print(star,end=" ")
        star=star+1
    print()

#17
#we can do this program in two types
#this is 1st method its some tough
class container:
    def addition(self,a,b):
        sum=a+b
        print("sum is:",sum)
    def subtraction(self,a,b):
        dif=a-b
        print("difference is:",dif)
    def multiplication(self,a,b):
        mul=a*b
        print("mul is:",mul)
    def didvison(self,a,b):
        div=a/b
        print("division",div)
num1=int(input("enter two numbers"))
num2=int(input())
num=int(input("1:addition\n2:subtraction\n3:multiplication\n4:division\nenter your choice"))
obj=container()
if num==1:
    obj.addition(num1,num2)
elif num==2:
    obj.subtraction(num1,num2)
elif num==3:
    obj.multiplication(num1,num2)
elif num==4:
    obj.didvison(num1,num2)
else:
    print("invalid number")

#this is 2nd method
#this is some easy
class container:
    def addition(self,a,b):
        sum=a+b
        return sum
    def subtraction(self,a,b):
        dif=a-b
        return dif
    def multiplication(self,a,b):
        mul=a*b
        return mul
    def didvison(self,a,b):
        div=a/b
        return div
    def invalid(self):
        return "invalid number"
num1=int(input("enter two numbers"))
num2=int(input())
num=int(input("1:addition\n2:subtraction\n3:multiplication\n4:division\nenter your choice"))
obj=container()
if num==1:
    result=obj.addition(num1,num2)
elif num==2:
    result=obj.subtraction(num1,num2)
elif num==3:
    result=obj.multiplication(num1,num2)
elif num==4:
    result=obj.didvison(num1,num2)
else:
    result=obj.invalid()

print(result)

#18
print(495000*5/100)
print("enter the mark scored by the students")
writtentest=int(input("written test="))
labexams=int(input("lab exams="))
assignments=int(input("assignments="))
grade=(writtentest*70)/100+(labexams*20)/100+(assignments*10)/100
print("aruns garde is:",grade)



#19
income=int(input("please enter you annual income:"))
if income<250000:
    print("NO TAX")
elif income>250000 and income<=500000:
    tax=income*5/100
    print("income tax amount is:",tax)
elif income>500000 and income<=1000000:
    tax=income*20/100
    print("income tax amount is:",tax)
elif income>1000000 and income<=5000000:
    tax=income*30/100
    print("income tax amount is:", tax)


#27
list1=[1,2,3,4]
list2=[]
square=lambda x:x*x
cube=lambda x:x*x*x
for i in list1:
    print(f"square of:{i} is :{square(i)}")
    print(f"cube of  :{i} is :{cube(i)}")
    list2.append(square(i))
    list2.append(cube(i))
print(list2)



str=input("enter a string")
str1=""


for i in str:
    if i not in str1:
        str1=str1+i
        fr=str.count(i)
        print(f"count of {i} is {fr}")

r=int(input("enter rows"))
c=int(input("enter cols"))
l=[]
m=[]
for i in range(r):
  l=[]
  print(f"enter {i+1}st row")
  for j in range(c):
    v=int(input())
    l.append(v)
  m.append(l)
print(m)


#22
models=[{'name':'sabah','age':23},{'name':'irfan','age':20},{'name':'aslah','age':19},{'name':'safwan','age':25}]
print(models)
new={}
new=sorted(models,key=lambda x:x['age'])
print(new)
'''

# #30
# count=0
# f=open('/home/sabah/sabaheeee','r')
# for i in f:
#     count+=1
# print(count)
#
# #

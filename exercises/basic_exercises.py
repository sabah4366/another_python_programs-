#2
num=int(input("enter a number"))
pn=0
for i in range(num):
    cn=i
    sum=cn+pn
    print(f"current number is:{cn}\tprevious number is{pn}\tsum is:{sum}")
    pn=i

'''
#3
st=input("enter a string")
for i in range(0,len(st),2):
    print(st[i])


#4
def string(word,n):
    print(word)
    f=word[n:]
    return f

print(string("pynative",4))




#5
lst=[3,2,3,4,5,6,2,3]
def fnctn(lstt):
    for i in lstt:
        firstnum=lstt[0]
        lastnum=lstt[-1]
        if firstnum==lastnum:       #this is first condition
        #if i==lstt[len(lst)-1]:     #this is second condition
            return True
        else:
            return False
print("result is:",fnctn(lst))


#6
lst=[10,20,34,40,50,60]
for i in lst:
    if i%5==0:
        print(i)

#7
str="emma is a good developer and emma is a writer. emma".split()
print(str.count('emma'))



#9
num="127"
s=len(num)
flag=0
for i in range(s):
    if num[i]!=num[s-i-1]:
        flag=1
        break
if flag==1:
    print("not")
else:
    print("pal")


#10
lst1=[1,2,3,4,5,6]
lsr2=[20,25,30,35,40,45]
lst3=[]
for i in lst1:
    if i%2!=0:
        lst3.append(i)
for i in lsr2:
    if i%2==0:
        lst3.append(i)
print(lst3)


#11
nu=7536
print(nu)
while nu>0:
    digit=nu%10
    nu=nu//10
    print(digit,end=" ")

#12
for i in range(1,11):
    for j in range(1,11):
        print(f"{i*j}",end=" ")
    print()

#13
lmt=5
lmt2=5
for i in range(lmt):
    for j in range(lmt2):
        print("*",end=" ")
    lmt2=lmt2-1
    print()

#14
def fun(b,e):
        return b**e

base=int(input("enter base number"))
exponent=int(input("enter exponent number"))
print(f"{base} raises to the power of {exponent} is: {fun(base,exponent)}")
'''

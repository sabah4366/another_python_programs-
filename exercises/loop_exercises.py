'''
#1
num=12345345
count=0
while num>0:
    num=num//10
    count=count+1
print(count)


#fibinocci series\
f=0
s=1
for i in range(10):
    print(f)
    t=f+s
    f=s
    s=t
#factorial
num=5
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)

#reverse
num=12345
while num>0:
    d=num%10
    num=num//10
    print(d,end="")

#list print odd
lst=[10,20,30,40,50,60,70,80,90,100]
for i in lst[1::2]:
    print(i)



#cube
num=10
for i in range(1,num+1):
    c=i**3
    print(f"current numbers is:{i}\tcube is{c}")

#2+22+222+2222+22222=sum
tr=5
st=2
val=0
for i in range(tr):
    print(st,end='+')
    val=st+val
    st=(st*10)+2
print(f"\ntotal value is:{val}")
'''
#pattern
lmt=5
sp=6
for i in range(1,2*lmt+2):
    for j in range(1,sp+1):
        print("*",end="")
    if i>lmt:
        sp=sp+1
    else:
        sp=sp-1
    print()



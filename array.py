import array as arr
'''accept an two array from the user, and swapping that two array ,and user enter a value in the first array
check that value is in which index then print that index
'''
'''
#accept an array from the user

lmt=int(input("enter the limit of an array"))
print("enter the values of first array")
arry1=arr.array('i',[])
arry2=arr.array('i',[])
arry3=arr.array('i',[])
for i in range(lmt):
    x=int(input())
    arry1.append(x)
print(arry1)


#this is two array swapping
lmt=int(input("enter the limit of an array"))
print("enter the values of first array")
arry1=arr.array('i',[])
arry2=arr.array('i',[])
arry3=arr.array('i',[])
for i in range(lmt):
    x=int(input())
    arry1.append(x)
print("enter the values of second  array")
for j in range(lmt):
    y=int(input())
    arry2.append(y)
arry1,arry2=arry2,arry1  #swapping array
print("first array is",arry1)
print("second array is",arry2)


#this is for swapping and  search a element in the array and print the index
lmt=int(input("enter the limit of an array"))
print("enter the values of first array")
arry1=arr.array('i',[])
arry2=arr.array('i',[])
arry3=arr.array('i',[])
for i in range(lmt):
    x=int(input())
    arry1.append(x)
print("enter the values of second  array")
for j in range(lmt):
    y=int(input())
    arry2.append(y)
arry1,arry2=arry2,arry1  #swapping array
print("first array is",arry1)
print("second array is",arry2)
srch=int(input("enter the search value in first array "))
temp=0
for i in arry1:
    if i==srch:
        print(f"index number of {srch} is {temp}")
        break
    temp+=1

#this is for array extend 
lmt=int(input("enter a limit "))
print("enter the values of an array ")
ar=arr.array('i',[])
for i in range(lmt):
    val=int(input())
    ar.append(val)
r=ar.extend([10,11])
print(ar)


#this for array insert
lmt=int(input("enter a limit "))
print("enter the values ")
arry1=arr.array('i',[])
for i in range(lmt):
    val=int(input())
    arry1.append(val)
print(arry1.insert(3,45))
print(arry1)



#removing an element from the aray
lmt=int(input("lmt"))
print("enter the values")
ar1=[]
for i in range(lmt):
    val=int(input())
    ar1.append(val)
ar1.pop()
print(ar1)

#array concatenation and slicing and all above functions
lmt=int(input('enter limit'))
print("enter values of first array")
arr1=[]
arr2=[]
arr3=[]
for i in range(lmt):
    val=int(input())
    arr1.append(val)
print('enter the values of 2nd array')
for i in range(lmt):
    val=int(input())
    arr2.append(val)
arr3=arr1+arr2
arr3.append(9)
arr3.extend([10,11])
arr3.insert(0,100)
print("concatenated array:",arr3)
print(arr3[::-1])
print(arr3[-2:-6:-1])


#array through for loop
a=[]
lmt=int(input('enter the array limit'))
print("enter the values")
for i in range(lmt):
    val=int(input())
    a.append(val)
print(a)
for i in a:
    print(i)


#####
a=[]
lmt=int(input("enter array limits"))
for i in range(lmt):
    val=int(input("=>"))
    a.append(val)
print(a)
srch=int(input("enter search value"))

def binary(a,srch):
    low = 0
    high = len(a) - 1
    mid = 0
    while low<=high:
        mid=(low+high)//2
        if a[mid]>srch:
            high=mid-1
        elif a[mid]<srch:
            low=mid+1
        else:
            return mid
    else:
        return -1
res=binary(a,srch)
if res==-1:
    print("not found ")
else:
    print("found")
'''



#
print("enter first matrix")
row=int(input("enter rows"))
cols=int(input("enter coloumns"))
a=[]
b=[]
for i in range(row):
    b=[]
    print(f'enter the {i+1} row elements')
    for j in range(cols):
        val=int(input("=>"))
        b.append(val)
    a.append(b)

c=[];d=[]
print("enter the matrix")
row=int(input("enter rows"))
cols=int(input("enter coloumns"))
for i in range(row):
    d=[]
    print(f'enter the {i+1} row elements')
    for j in range(cols):
        val=int(input("=>"))
        d.append(val)
    c.append(d)
print(a)
print(c)
s=[]
v=[]

for i in range(len(a)):
    for j in range(len(c)):
        f=a[i][j]+c[i][j]
        v.append(f)
    s.append(v)


print(v)
key=int(input('enter the key you want search'))
for i in v:
    if key==i:
        print(key,'found')
        break
else:
    print(key,'not found')


#
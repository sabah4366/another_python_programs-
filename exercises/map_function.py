'''#map functiion
def fun(x,y):
    return x+y,x-y


lst1=[3,5,8,10,71]
lst2=[1,2,3,4,5]
new=list(map(fun,lst1,lst2))
print(new)


#

list1=[1,2,3,4,5]
tuple1=(1,2,3,4,5)
lst=list(map(str,list1))
lst3=tuple(map(str,tuple1))
print(lst3)
print( lst)

#
lst=[('sabah','4-11-1999','22'),('irfan','12-3_2001','20'),('aslah','14-6-2002','21')]
newlst=list(map(lambda x:x[0],lst))
print(newlst)
newlst1=list(map(lambda x:x[1],lst))
print(newlst1)
newlst2=list(map(lambda x:x[2],lst))
print(newlst)

#
lst1=[1,2,3]
lst2=[1,2,3]
lst3=[1,2,3]
lst4=list(map(lambda x,y,z:x+y+z,lst1,lst2,lst1))
print(lst4)



#
lst=['red','blue','green']
nwlst=list(map(list,lst))
print(nwlst)


#
lst1=[10,20,30,40,50,60,70,80]
lst2=[1,2,3,4,5,6,7,8]
lst3=list(map(lambda x,y:x**y,lst1,lst2))
print(lst3)



#
import array as arr
ar1=arr.array('i',[1,2,3,4,5,-15])
print("array is:",ar1)
def summ(n):
    sum=0
    for i in n:
        sum=sum+i
    return sum

lst=summ(ar1)
print(lst)



#ratio of positive and negative and zeros of a given list
#  1:-how to calculate the ratio of postive numbers
#  1ans:-first count the postive numbers and last divided with the length of the all list
from array import *
ar1=array('f',[0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
def ratios(num):
    n=len(num)
    n1=n2=n3=0
    for i in num:
        if i>0:
            n1+=1
        elif i<0:
            n2+=1
        else:
            n3+=1
    return round(n1/n,2),round(n2/n,2),round(n3/n,2)

re=ratios(ar1)
print(re)



#
from operator import eq
lst1=[1,2,3,4,5,6]
lst2=[1,3,6,4,7,8]
def same(x,y):
    res=sum(map(eq,x,y))
    return res

lst3=same(lst1,lst2)
print(lst3)



#'red','pink'  to 'redpink'
lst=[('red','pink'), ('white','black'), ('orange','green')]
newlst=list(map(''.join,lst))
print(newlst)
'''



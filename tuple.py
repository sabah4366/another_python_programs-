'''d=("hai","hello","how","hey")

if "hai" in d:
    print("hai prescent in d")


print(d)
print(len(d))
print(type(d))
print(d[1])
print(d[1:3])
print(d[:3])
print(d[1:])
print(d[-4:-1])

y=list(d)
y[1]="mango"
y.append("orange")
y.remove("how")
d=tuple(y)
s=("pineaaple",)
d+=s
print(d)

#packin
fruits=("hai","hello","how","wow")      #this is packing

#unpacking
fruits=("hai","hello","how","wow")
(green,yellow,red,white)=fruits         #this is unpacking,you must check no.of variables must match no.of items in the tuple
print(green,yellow,white,red)

#you can use with asterrisk
fruits=("hai","hello","how","wow")
(green,*yellow)=fruits         #this is unpacking,if  no.of variables do not match with no.of itens in tuple then use asterisk
print(green,"\n",yellow)           #asterrisk variables items are placed on a list

#using tropic
fruits=("hai","hello","how","wow")
(green,*tropic,red)=fruits
print(green,tropic,red)

#using for loop
s=("hai","hello","how","wow")
for i in s:
    print(i)

#using for loop with index numbers
s=("hai","hello","how","wow")
for i in range(len(s)):
    print(s[i])

'''
#using while loop
s=("hai","hello","how","wow")
i=0
while i<len(s):
    print(s[i])
    i+=1

#join tuples
s=("hai","hello","how","wow")
f=(1,2,3,4,5)
print(s+f)

#multiply tuple
s=("hai","hello","how","wow")
print(s*2)
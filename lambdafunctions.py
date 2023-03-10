#some examples of lambda functions
s=lambda a:a*10
print(s(3))

#another one with two values
d=lambda a ,b:a*b
print(d(12,2))

#sumarize of thre values
f=lambda q,w,e:q+w+e
print(f(2,4,6))


#lambda using functions with classes
def hai(n):
    return lambda a:a*n
g=hai(10)
print(g(2))


#another example of lambda using functions
def sum(n):
    return lambda a,b,c:(a+b+c)*n
s=sum(2)

print(s(2,4,6))


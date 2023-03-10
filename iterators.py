'''#iterator in tuple
s=("apple","banana","orange")
d=iter(s)

print(next(d))
print(next(d))
print(next(d))

#iterator in string
st="pallipparamb"
d=iter(st)
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))

#iterator through for loop
f=["hai","hey","how"]
for i in f:
    print(i)



#iterator using class functions
class Myclass:
    def __iter__(self):
        self.a=5
        return self
    def __next__(self):
        x=self.a
        self.a=self.a+1
        return x

hai=Myclass()
hey=iter(hai)
print(next(hey))
print(next(hey))
print(next(hey))
print(next(hey))
print(next(hey))
print(next(hey))
'''
#stopiteration
class Myclass:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a <=20:
            x=self.a
            self.a=self.a+1
            return x
        else:
            raise StopIteration

hai=Myclass()
hey=iter(hai)
for i in hey:
    print(i)
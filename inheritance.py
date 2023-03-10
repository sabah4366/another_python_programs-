class first:
    def __init__(self,name,age):
        self.age=age
        self.name=name
        print(age)
        print(name)
        print("first class in it ")



    def display(self,name,age):
        self.name=name
        self.age=age
        print("name is:",name)
        print("age is :",age)
        print("first class display")

class second(first):
    def __init__(self):
        super().__init__(name=any,age=any)
        print("second class init")

    def display(self,name,age):
        super().display(name,age)
        print("second classs display")




        print("second class display")

  

    def hai(self,name,age,place):
        self.a=name
        self.v=age
        self.d=place
        print(self.a)
        print(self.v)
        print(self.d)
        print("hai")


a=second()
a.display("sabah",21)



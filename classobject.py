class my_class:
    year=2022
    def __init__(self,name,age,place):
        self.age=age
        self.name=name
        self.place=place


    def add_age(self):
        self.age=self.age+1



    @classmethod            #class method ullil ulle method call chyyuka classname vechhitt aan
    def addyear(cls):
        cls.year=cls.year+1

    @staticmethod           #static method ullil ulle method call chyyuka classname vechhitt aan
    def display_a_text():
        print("welcome to the page")


    def details(self):

        print("name is:",self.name)
        print("age is",self.age)
        print("place is",self.place)
        print("year is", my_class.year)
    def relocation(self,place):
        self.place=place


x=my_class("dilshad",23,"kakkanad")
y=my_class("sabah",21,"kannur")
my_class.display_a_text()
x.details()
print()
y.details()

my_class.addyear()
x.add_age()
y.add_age()
x.relocation("calicut")
y.relocation("kochin")
print("--------------------------")

x.details()
y.details()



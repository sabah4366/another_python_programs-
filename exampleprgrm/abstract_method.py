from abc import ABC,abstractmethod
class Main:
    def values(self):
        self.num1=int(input("enter 2 numbers"))
        self.num2=int(input())
    def sum(self):
        sum=self.num1+self.num2
        print(sum)

    @abstractmethod
    def examples(self):
        print("hai")
obj=Main()
obj.values()
obj.sum()
obj.examples()


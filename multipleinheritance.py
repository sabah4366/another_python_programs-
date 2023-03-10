class First:
    def sum(self):
        print("first class sum")

    def display(self):
        print("first claass diplay")


class Second:
    def equal(self):
        print("second class equal")

    def display(self):
        print("second claass diplay")

class Third(First,Second):
    def equal(self):
        print("third class equal")



a=Third()
a.equal()
a.display()
print(Third.mro())
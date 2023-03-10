class A:
    def __init__(self):
        print("first init ")
    def first(self):

        print("thiis is first function")



class B(A):
    def __init__(self):
        super().__init__()
        print("second init")
    def second(self):
        print("this is second function")


class C(B):
    def __init__(self):
        super().__init__()
        print("third init")
    def third(self):
        print("this is third function")


a=C()
a.first()
a.second()
a.third()

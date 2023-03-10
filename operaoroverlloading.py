class A:
    def  display(self,name):
        self.a=name



    def __add__(self, other):
        d=self.a+" "+other.a
        return d


af=A()
bs=A()
d=af.display("sabah")
d=bs.display("irfan")
c=af+bs
print(c)
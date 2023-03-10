
class All:
    def fun(self, switch):
        match switch:
            case 1:
                return "sunday"
            case 2:
                return 'MONDAY'
            case 3:
                return "tuesday"
            case 4:
                return "wednesday"
            case 5:
                return "thursday"
            case 6:
                return "friday"
            case 7:
                return "saturday"
            case wrong:
                return "wrong choice"
ob=All()
print("1:sun\n2:mon\n3:tue\n4:wed\n5:thur\n6:fri\n7:satr")
try:
    n=int(input("enter number"))
    s=ob.fun(n)
    print(s)
except ValueError:
    print("must enter integer")
else:
    print("finish")

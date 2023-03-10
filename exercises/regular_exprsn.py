import re
def expressions(st):
    s='^a(b*)$'
    if re.search(s,st):
        print("found")
    else:
        print('not')
print(expressions("ab"))
print(expressions("hai rothe hy"))


#

def swap_num(fn):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapper
@swap_num
def sum(n1,n2):
    return n1-n2
print(sum(5,10))
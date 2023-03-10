
def hey(a):

    if a>0:
        sum=a-(a*hey(a-1)+1)
        print(sum)
        return sum
    else:
        return 0




hey(3)

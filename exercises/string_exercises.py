'''
#1
str="james"
print(str[0:5:2])

#2
c1="jhondippeta"
c2="jasonpy"
c=int(len(c1)/2)
d=int(len(c2)/2)
print(c1[c-1:c+2:1])
print(c2[d-1:d+2:1])

#3

s1="ault"
s2="kelly"
m=int(len(s1)/2)
x=s1[:m:]
x=x+s2[::]
x=x+s1[m:]

print(x)
'''

# 4
s1 = "America"
s2 = "Japan"
s1m = int(len(s1)/2)
s2m = int(len(s2)/2)
x = s1[:1:] + s2[:1:]
x = x + s1[s1m:s1m+1]+s2[s2m:s2m+1]
x=x+s1[-1]+s2[-1]
print(x)


#5
# str='12jhon is 2developer 3musician'
# for i in str:
#     if i.isdigit():
#         str.replace('#')
        
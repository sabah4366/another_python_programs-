'''#1 two list converted to a dictionary
lis=['ten','twenty','thirty']
lst1=[10,20,30]
lst3=dict(zip(lis,lst1))
print(lst3)

#2 two list cinverted to a dictionary
lis=['ten','twenty','thirty']
lst1=[10,20,30]
lst=dict()
for i in range(len(lis)):
    lst.update({lis[i]: lst1[i]})
print(lst)




#merge
s={'ten': 10, 'twenty': 20, 'thirty': 30}
b={'ten': 10, 'fifty': 50, 'fourty': 40}
c={**s,**b}
print(c)


#other type of merge
s={'ten': 10, 'twenty': 20, 'thirty': 30}
b={'ten': 10, 'fifty': 50, 'fourty': 40}
c=s.copy()
c.update(b)
print(c)
'''

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
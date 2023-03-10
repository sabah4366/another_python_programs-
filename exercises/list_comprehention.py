# #1
# lst=[i for i in range(1200,2000,130)]
# print(lst)
#
#
# #2
# lst=[2,4,6,8,10,12 ,14]
# lst2=[i*i for i in lst if i*i>50 ]
# print(lst2)
#
# #3
# dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7,
#       "Motorcycle": 110}
# lst2=[i for i in range(len(dict))]
# print(lst2)

#4
# str="hai sabah how are you"
# lst=''.join([i for i in str  if i not in "aeiouAEIOU"])
# print(lst)


#5

# strn="i need to find a tree palllli to piss off ".split()
# lst=[i for i in strn if len(i)<5]
# print(lst)


lst=[1,23,46,23,65,78,56]
lstnw=[i for i in lst if '6' in str(i)]
print(lstnw)

#1
dict={}
lmt=int(input("enter the limit"))
for i in range(lmt):
    name=input("enter the name ")
    salary=int(input("enter the salary"))
    if name not in dict:
        dict[name]=salary
print(dict)


#2
# lst=['apple','orange','grapes','kiwi','apple','orange']
# dict={}
# for i in lst:
#     if i not in dict:
#         dict[i]=1

#     else:
#         dict[i]=dict[i]+1

# dict["apple"]=5
# print(dict)

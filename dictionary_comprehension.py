#this is one method a lst and lst1 converted into a dictionary using dictionary comprehension
lst=[1,2,3,4]
lst1=['sabah','irfan','aslah','afsal']
dct={lst[i]:lst1[i] for i in range(len(lst1))}
print(dct)
#
# #this is dictionary comprehension
# dct2={i:j for i,j in zip(lst,lst1)}
# print(dct2)

#
# lst3=['apple','apple','banana','orange','banana']
# dct={}
# for i in lst3:
#     if i not in dct:
#         dct[i]=1
#     else:
#         dct[i]=dct[i]+1
# print(dct)
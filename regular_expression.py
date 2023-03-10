import re
# #re.findall
# find=re.findall("hai","hai iam sabah hai irfan")
# for i in find:
#     print(i)

# #RE.FINDITER
# #re.finditer function
# #it is print starting and ending index of the matching object
# st="hai iam sabah from pallipparamba hai"
# for i in re.finditer("hai",st):
#     tup=i.span()
#     print(tup)



# #RE.FINDALL
# #re.findall function
# #finding "ai" in this list and print that "ai" in a list format
# #if "ai" is not found then the empty list will returned
# s="hai hello haiii hey hoai"
# x=re.findall("ai",s)
# print(x)



# #RE.SEARCH
# #re.search function
# #search function will search the string of a match and returned math object if there is a match
# #if there is more than one match then the first occurence only take
# text="hey how are you hey iam fine heyhow"
# text1=re.search("haaaa",text)    #if there is no match then none value will be returned
# text2=re.search("\s",text)      #\s means returns a match the whitespace character
# print(text1)
# print(text2.start())   #start() this means starting index position


#RE.SLPIT
#re.split function
#split function will returns where the string has been slpit at each match
#you can also split with numbering that is :--- re.split("\s",variablename,1)
text3="there is no second chance there is only this last chance "
text4=re.split("is",text3)      #this "is" will remove and split at the position of "is" and give a splitted list
text5=re.split("\s",text3)      #this will split at the position space because "\s" is a space
text6=re.split("\s",text3,1)    #this will split when the first occurence of white space
print(text4)
print(text5)
print(text6)

# #RE.SUB
# #this function is replaces the matches with  the text of your choice
# text7="hey man how are you iam fine"
# text8=re.sub("man","sabah",text7)    #this means the man position is replaces with sabah
# print(text8)
# text9="i idont know who are you"
# text10=re.sub("\s","12",text9,2)    #this means the space position replaces with 12 and that 12 placed at 1st and 2nd postionn of space
# print(text10)                       #that last 2 means -namukk 12 eth index vare kodkkanun ariyaan vendi


# #MATH OBJECT
# #if there is no match then none will be returned instead of the math object
# text11="the rain  in spain"
# text12=re.search('ain',text11)      #this will print the a math object
# print(text12)

# #the math object has properties and method to retrieve the information of the search and the result
# #that are .span() and  .string() and .group()
# #.span() is returns a tuple with the start and end position of the match
# #.string() is returned the string passed into the function
# #.group() is returns the part of the string where there was a match

# #.SPAN()
# text13="the rain in spain"
# text14=re.search(r"\bs\w+",text13)  #this will print start and endindex of the 's'
# print(text14.span())

# #.STRING()
# #The string property returns the search string:
# text15="the rain in spain"
# text16=re.search("s",text15)
# print(text16.string)

# #.GROUP()
# #print the part the part of the sting where there was a match
# text17="the rain in spain"
# text18=re.search(r"\bs\w+",text17) #this means for any words starts with lower case 's' and 's' kainitt ulle chatacters print chyum
# print(text18.group())               #first occurence of lower case 's' will print


# #using dot(.)
# str='123abcd345ugf'
# pattern=re.compile(r'.')
# matches=pattern.finditer(str)
# for i in matches:
#     print(i.group())


# #using dot(.)
# str='123abcd345ugf.'
# pattern=re.compile(r'\.')   #this will print only dot
# matches=pattern.finditer(str)
# for i in matches:
#     print(i.group())


# #start(^)
# #^ means start
# s='hai sabah how old are you :23'
# pattern=re.compile('^hai')
# matches=pattern.finditer(s)
# for i in matches:
#     print(i.group())

# #end($)
# #  $ means end
# s='hai sabah how old are you :23'
# pattern=re.compile('23$')
# matches=pattern.finditer(s)
# for i in matches:
#     print(i.group())



# strng='hai hey how 123_'
# pattern=re.compile(r'[a-z]')
# matches=pattern.finditer(strng)
# for i in matches:
#     print(i)

# #it will matches non digit character
# print('------------------')
# strng='hello_ 123world'
# p=re.compile(r'\d')
# matches=p.finditer(strng)
# for i in matches:
#     print(i)



# d='''
# 2000-12-02
# 2000-12-03
# 1999-12-23

# 2000/12/02
# 2000/12/04
# 1999/11/23

# 2000.12.02
# 2000.12.03
# 1999.11.23
# '''
# print(d)
# p=re.compile(r'\d\d\d\d/\d\d/\d\d')
# s=p.finditer(d)
# for i in s:
#     print(i)

# p=re.compile(r'\d\d\d\d-\d\d-\d\d')
# s=p.finditer(d)
# for i in s:
#     print(i)
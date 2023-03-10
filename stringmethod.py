num="hai my name is sabah"
lists=["hello","my","name","is","sabah"]
print(num.casefold())   #is the string is capital then it will make all small
print(num.capitalize()) #it will make first letter capital
print(num.rsplit(' ',maxsplit=1))   #it will split 2sections, right side n split chyyum ,right sidle first word split chythit baaaki ellu vera sectionl idum
s='_'.join(lists)  #this is join section,join the lists
print(s)
print(num.islower())  #to check the string is lower if it is lower then output is true otherwise false
print(num.isupper()) #to check the string is uppper if its upper then output is true otherwise false
word="sabah"
word2="1234"
print(word.isalnum()) #to check the string is alphabetic or numeretic ,then output is true otherwise false
print(word.isalpha())   #to check the string is alphabetic ,then output is true otherwise false
print(word2.isnumeric())    #to check the string is numeretic ,then output is true otherwise false
print(num.count('a'))       #to count the number of arguement that passed


idx=num.find('n')       #to find in which index number the argement is standing
print(idx)
print(num[idx:])        #to display index number to end
print(num.startswith('hai'))    #to check it start with hai,if it is corect,output true otherwise false
print(num.endswith('ah'))       #to check it end with sabah,if it is corect,output true otherwise false
print(num.partition('name'))    #for partition
print(num.center(26,'-'))       #the strung will stand center
print(num.ljust(30,'-'))        #the string will stand leftside
print(num.rjust(27,'-'))        #the string will stand right side
word1="mabn MAN"
print(word1.swapcase())         #the string swap
print(word1.zfill(12))          #fill 0s with beginning
print(num.title())              #this is for capitakize each word
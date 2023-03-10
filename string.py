name="banana"  #this is string
print(name) #that string printing
print(len(name)) #length of that string
print(name[2]) # 2 means character of that 2nd postion
print('b' in name)  #to check b is prescent in name
print('n' not in name) #to check n not in name
if 'ba'  in name:                           #to check use if conditon 'ba' is prescent in name
    print("yes 'na ' prescent in name")


if "sa" not in name:                        #to check use if condition 'sa' not prescent in name
    print("yes 'sa' not prescent in name ")


#slicing typess
h="hello world"
print(h[1:5])         #slicing
print(h[:7])          #slicing from the start
print(h[2:])          #slicing to the end
print(h[-10:-4])       #negative indexing

#modify strings
d="iam sabah k"
print(d.upper())               #string to upppercase letters
print(d.lower())               #string to lowercase letters
print(d.split())            #split the string
print(d.replace("ia" ,"sa"))   #replace the string
print(d.rstrip())

#string  concatination
a="iam"
b="sabah"
c=a+" "+b       #you want to add a space between twon strings put a double quotes
print(c)

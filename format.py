#string combining using format method
name="sabah"
age=24
place="kannur"
details="my name is {} and iam {} years old and iam from {}"  # inside the braces you can use index numbers
print(details.format(name,age,place))           #index number 0-name,indecxnumber1-age,indexnumber2-place


#this is the other way of string combining
name="sabah"
age=11
place="kannur"
details=f"my name is {name} and iam {age*2} years old and iam from {place}"
print(details)



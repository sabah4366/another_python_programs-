values=["apple","banana","mango","jackfruit"]
print(type(values))
print(values) #for printing list values
print(values[-1]) #-1 means last value in a list
print(values[3]) #this is same as upper statement this 3rd value but uppper case -1 that is also last value
print(values[2:]) #this will display  2nd postion to end valuse
print(len(values)) #this is for identify the length of the list
values=values+["pomegranate","grapes",2] #this is for adding three values to the list
print(values)
values.append("passionfruit") #this is for adding a value  at last position
print(values)
values.append(input("enter a value to the list")) #this is for recieving a value from user to the last postion
print(values)

if "Banana" in values:           #this is finding a item is prescent in the list
    print("yes bnanana is prescent in the values")
else:
    print(" banana not prescent in the values" )


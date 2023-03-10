
# no arg no return
def display():
    print("this is display function")


display()




# arbetary element
def add(*values):   #that star(*) means arbetary it means we can pass multiple parameters in a single argument
    print(values)   #this is for print all parameters
    print(values[0])    #this is for print that 0th index only


add("hai", "hey", "hello")


# keywordargument
def keywrd(name, age):
    print("name is:" + name + "\nage is:" + str(age))


keywrd(age=12, name="sabah")


# default argument
def default(name, age=32):
    print("name is "+name+"\nage is "+str(age))


default(name="marwa")           #in this function calling the output is marwa 32
default(name="marwa",age=12)    #in this function calling the output is marwa 12

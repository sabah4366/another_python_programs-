from users.models import employees
from operator import itemgetter
for emp in employees:
    print(emp['name'],":",emp["salary"])


#print employee names whose salary greater than 25000
print("salary greater than 25000")
for emp in employees:
    if emp["salary"]>25000:
        print(emp["name"])
#using list comprehension above program
print(" print employee names whose salary greater than 25000 \n-------------------------")
lst=[emp["name"] for emp in employees if emp["salary"]>25000]
print(lst)

#questions
#print employee names who are working in dept devop
print("devop only\n-----------")
for emp in employees:
    if emp["dept"]=='devop':
        print(emp["name"])


# using list comprehension above program
print("print employee names who are working in dept devop\n-------------------------")
lst=[emp["name"] for emp in employees if emp["dept"]=="devop"]
print(lst)


#highest salaried employee
print("highest salary employee\n-------------")
for emp in employees:
    num=emp["salary"]
    name=emp["name"]
    break

for emp in employees:
    if emp["salary"]>num:
        num=emp["salary"]
        name=emp["name"]
print(name,num)



#highest salaried employee using max(),
print("highest salary employee\n-------------")
print(max(employees,key=lambda emp:emp["salary"]))


#sort employes based on salary order by desc
print("sorted order by salary using lambda function\n-------------------------------------------- ")
sorted_models = sorted(employees, key = lambda x: x['salary'] ,reverse=True)
print(sorted_models)


#we can sort using another method using operator module
#use itemgetter in that madule
print("sorted order by salary using operator module\n-------------------------------------------- ")
#newdict=sorted(employees,key=itemgetter("salary"),reverse=True)      #also use this way but it will take add
employees.sort(key=itemgetter('salary'),reverse=True)
print(employees)



#greater number-lesser number
print("greater number-lesser number")
def smart_sub(num1,num2):
    if num1>num2:
        return num1-num2
    else:
        return num2-num1
print(smart_sub(8,4))

#solve above function using easiest method
print("solve above function using easiest method")
n1=10
n2=20
print(n1-n2 if  n1>n2 else n2-n1)

#solve above function using lambda function
print("solve above function using lambda function")
smart=(lambda n1,n2:n1-n2 if n1>n2 else n2-n1)
print(smart(20,40))


#find even or odd
print("find even or odd")
odd_even=lambda n:"even" if n%2==0 else "odd"
print(odd_even(3))


#show salary
print("show salary")
data={"id":100,"name":"sabah","salary":12000}
get_sal=lambda emp:emp["salary"]
print(get_sal(data))



#new question
users = [
    {"id": 1, "name": "akhil", "following": [2, 5, 6]},
    {"id": 2, "name": "anu", "following": [7, 8]},
    {"id": 3, "name": "vinu", "following": [1, 3, 4]},
    {"id": 4, "name": "tinu", "following": [4, 5, 6, 7]},
    {"id": 5, "name": "ram", "following": [5, 6, 7]},
    {"id": 6, "name": "revin", "following": [1, 2, 3]},
    {"id": 7, "name": "raj", "following": [5, 7, 8]},
    {"id": 8, "name": "gokul", "following": []},
    {"id": 9, "name": "rohan", "following": [1, 2, 3]},
    {"id": 10, "name": "jitu", "following": [1, 2, 3, 4, 5, 6, 7, 8]},

]
posts = [
    {"pid": 1, "title": "goodmorning", "author": 5, "liked_by": [2, 3, 4]},
    {"pid": 1, "title": "hello guyz", "author": 4, "liked_by": [2, 3, 7, 8]},
]


#which user has most number of followers,etc






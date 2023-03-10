#if and else and elif controlstructures

num = int(input("enter a  number "))
("you must convert the value to the integer because we  write only input then the it will get an error because that \n"
 "input value is string type so must convert to int")
if num >= 1:
    print("entered number is positive")
elif num == 0:
    print("the  entered number is 0")

elif num < 0:
    print("entered number is negative")

else:
    print("invalid chararter")

#program for a hotel menu
print("1-biriyani\n2-mandhi\n3-poratta")
num=int(input("enter your choice "))
if num==1:
    print("you selected biriyani")
elif num==2:
    print("you selected mandhi")
elif num==3:
    print("you selected porotta")
else:
    print("invalid")
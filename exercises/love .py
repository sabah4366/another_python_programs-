# # Import turtle package
# import turtle
#
# # Creating a turtle object(pen)
# pen = turtle.Turtle()
#
#
# # Defining a method to draw curve
# def curve():
#     for i in range(200):
#         # Defining step by step curve motion
#         pen.right(1)
#         pen.forward(1)
#
#
# # Defining method to draw a full heart
# def heart():
#     # Set the fill color to red
#     pen.fillcolor('red')
#
#     # Start filling the color
#     pen.begin_fill()
#
#     # Draw the left line
#     pen.left(140)
#     pen.forward(113)
#
#     # Draw the left curve
#     curve()
#     pen.left(120)
#
#     # Draw the right curve
#     curve()
#
#     # Draw the right line
#     pen.forward(112)
#
#     # Ending the filling of the color
#     pen.end_fill()
#
#
# # Defining method to write text
# def txt():
#     # Move turtle to air
#     pen.up()
#
#     # Move turtle to a given position
#     pen.setpos(-20, 95)
#
#     # Move the turtle to the ground
#     pen.down()
#
#     # Set the text color to lightgreen
#     pen.color('white')
#
#     # Write the specified text in
#     # specified font style and size
#     pen.write("I LOVE YOU\n FATHII", font=(
#         "Verdana", 12, "bold"))
#
#
# # Draw a heart
# heart()
#
# # Write text
# txt()
#
# # To hide turtle
# pen.ht()

from turtle import *

import turtle as tur

turt = tur.Turtle()
tur.title("Pythontpoint")


def curve():
    for i in range(200):
        # Defining step by step curve motion
        turt.right(1)
        turt.forward(1)


def heart():
    # Set the fill color to red
    turt.fillcolor('red')

    # Start filling the color
    turt.begin_fill()

    turt.left(140)
    turt.forward(113)

    curve()
    turt.left(120)

    # Draw the right curve
    curve()

    turt.forward(112)
    turt.end_fill()


def txt():
    turt.up()
    turt.setpos(-68, 95)
    turt.down()
    turt.color('white')
    turt.write("I LOVE YOU\n FATHII", font=(
        "Verdana", 15, "bold"))


# Draw a heart
heart()

# Write text
txt()

# To hide turtle
tur.ht()
tur.done()
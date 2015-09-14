import turtle
import math

wn = turtle.Screen()
marcus = turtle.Turtle()

def calculate(user_input):
    x = 0
    y = 0
    
    if user_input != "nothing":
        change_input = int(input("What are you changing x by?"))
    
    if user_input == "inverse":
        x = 1
        marcus.up()
        marcus.goto(1,1)
        marcus.down()
    elif user_input == "add":
        marcus.up()
        marcus.goto(0,change_input)
        marcus.down()
    elif user_input == "subtract":
        marcus.up()
        marcus.goto(0,-change_input)
        marcus.down()
    
    while x < 201:
        if user_input == "constant":
            y = change_input
        elif user_input == "nothing":
            y = x
        elif user_input == "add":
            y = x + change_input
        elif user_input == "subtract":
            y = x - change_input
        elif user_input == "multiply":
            y = x * change_input
        elif user_input == "divide":
            y = x / change_input
        elif user_input == "inverse":
            y = change_input / x
        elif user_input == "power":
            y = x ** change_input
        elif user_input == "to the x":
            y = change_input ** x
        elif user_input == "root":
            y = x ** (1 / change_input)
        elif user_input == "sine":
            y = change_input * math.sin(x)
        elif user_input == "cosine":
            y = change_input * math.cos(x)
        elif user_input == "tangent":
            y = change_input * math.tan(x)
        elif user_input == "cosecant":
            y = change_input * (1 / math.sin(x))
        elif user_input == "secant":
            y = change_input * (1 / math.cos(x))
        elif user_input == "cotangent":
            y = change_input * (1 / math.tan(x))
        elif user_input == "logarithm":
            y = math.log(x,change_input)
        else:
            print "SYSTEM FAILURE"
        marcus.goto(x,y)
        x += 1

calculate(input("what do you want to do to x?"))
wn.exitonclick()

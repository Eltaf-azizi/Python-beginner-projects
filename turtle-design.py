import turtle
turtle.bgcolor("black")
squary = turtle.Turtle()
def design():
    squary.speed(20)
    squary.pencolor("red")
    for i in range(400):
        squary.forward(i)
        squary.left(91)
        
        


import turtle
import colorsys

t = turtle.Turtle()
def circle():
    s=turtle.Screen().bgcolor('white')
    t.speed(0)
    n = 70
    h = 0
    for i in range(360):
        c = colorsys.hsv_to_rgb(h, 1,   0.8)
    h += 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for i in range(2):
        t.left(2)
        t.circle(100)
  
  
a = 10
b = 9
if (a>b):
    design()
else:
    circle()
    


def add_mumber(a, b):
    return a * b

result = add_mumber(374, 732)

print(result)



def greet(name):
    print('hello, ' + name + '!')
    

greet("Altaf")


def add(num):
    return num * num
    

new = add(4)
print(new)
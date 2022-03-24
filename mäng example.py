#kodutöö kujund

import turtle

t = turtle.Turtle()
aken = turtle.Screen
k = turtle.Turtle()

a = 50
b = 90
c = 25
    
for i in range(5):
    k.forward(c)
    k.left(b)
    k.forward(a)
    k.left(b)
    k.forward(a)
    k.left(b)
    k.forward(a)
    k.left(b)
    k.forward(c)
    k.left(75)


aken.exitclickon()
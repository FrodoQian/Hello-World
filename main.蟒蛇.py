#pythonDraw.py
import turtle as t
t.setup(650,350,200,200)
t.penup( )
t.fd(-250)
t.pendown()
t.pensize(25)
t.pencolor(0.8,0.8,0.8)
t.seth(-40)
for i in range(4):
    t.circle(40,80)
    t.circle(-40,80)
t.circle(40,40)
t.fd(40)
t.circle(16,180)
t.fd(40)
t.done( )
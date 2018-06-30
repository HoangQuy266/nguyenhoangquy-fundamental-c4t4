from turtle import *

speed(-1)
color("blue")

for i in range(40):
    for _ in range(4):
        forward(50+i*2)
        left(90)
    right(10)

mainloop()
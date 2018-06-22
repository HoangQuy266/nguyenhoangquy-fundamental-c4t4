from turtle import *
speed(-1)
shape("turtle")
for i in range(10):
    for _ in range(4):
        forward(100+i*20)
        left(90)
    left(20)
mainloop()
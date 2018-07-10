from turtle import *

speed (-1)
shape("turtle")

for i in range (4,9,1):
    for j in range (i):
        if j % 2 == 1: 
            color ("red")
        else: 
            color ("blue")
        forward (100)
        left (360/i)
    

mainloop ()
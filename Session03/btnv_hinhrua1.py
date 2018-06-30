from turtle import *


shape("turtle")
speed(-1)

for i in range(3,8,1):
    if i==3: color ("red")
    if i==4: color ("blue")
    if i==5: color ("purple")
    if i==6: color ("light blue")
    for a in range (i):
        forward(100)
        left (360/i)
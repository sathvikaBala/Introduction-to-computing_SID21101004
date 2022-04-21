import math
angle=0
num=345/15 #numebr of times the while loop will run
while angle<=345:
    ang=angle*(3.14/180)    #math function accepts radian angle values, hence the angles are converted here to radians
    valsine=math.sin(ang)   #sine value of the angle
    vsine=round(valsine,4)  #rounding off to 4 decimals 
    valcos=math.cos(ang)    #cos value of the angle
    vcos=round(valcos,4)    #rounding off to 4 decimals
    angle+=15               #incrementing the angle by 15 degree

    print(angle,'   ',vsine,'   ',vcos)

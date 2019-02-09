#Bubble Level Assignment
#Name: René LaPointe Jameson
#Statement of Collaboration: I recevied assistance from Professor Jennifer Cross, I worked with Sofia Levy on this assignment

import math
import microbit

def get_x_value():
    x = microbit.accelerometer.get_x()
    return x
def get_y_value():
    y = microbit.accelerometer.get_y()
    return y
def get_z_value():
    z = microbit.accelerometer.get_z()
    return z

def get_degrees(radians):
    degrees=(radians*180/math.pi)
    return(degrees)
#start of mainscript
while True:
    x_acc= get_x_value()
    z_acc= get_z_value()
    y_acc= get_y_value()

    Angle_x= math.atan2(x_acc,(math.sqrt(y_acc**2+z_acc**2)))
    Angle_y= math.atan2(y_acc,(math.sqrt(x_acc**2+z_acc**2)))
    Angle_x_deg= get_degrees(Angle_x)
    Angle_y_deg= get_degrees(Angle_y)

    #Display
    if Angle_x_deg < -5:
        if Angle_y_deg>5:
            microbit.display.show(microbit.Image.ARROW_NE)
        elif Angle_y_deg<-5:
            microbit.display.show(microbit.Image.ARROW_SE)
        else:
            microbit.display.show(microbit.Image.ARROW_E)
    elif Angle_x_deg>5:
        if Angle_y_deg>5:
            microbit.display.show(microbit.Image.ARROW_NW)
        elif Angle_y_deg<-5:
            microbit.display.show(microbit.Image.ARROW_SW)
        else:
            microbit.display.show(microbit.Image.ARROW_W)
    else:
        if Angle_y_deg>5:
            microbit.display.show(microbit.Image.ARROW_N)
        elif Angle_y_deg<-5:
            microbit.display.show(microbit.Image.ARROW_S)
        else:
            microbit.display.show(microbit.Image.HAPPY)
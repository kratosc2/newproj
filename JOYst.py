from myro import *

buttons = getGamepad("button")
triangle = buttons[0]
circle   = buttons[1]
cross    = buttons[2]
square   = buttons[3]

print "Triangle:",triangle
print "Square:",square
print "Cross:",cross
print "Circle:",circle

while 1:

    axis = getGamepad('axis')
    lrb = axis[0]
    udb = axis[1]

    if not lrb == 0.0:
        if lrb >  0.0:
            print "Right"
        else:
            print "Left" 

    if not udb == 0.0:
        if udb > 0.0:
            print "Down"
        else:
            print "Up"




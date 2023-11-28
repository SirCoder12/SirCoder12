from turtle import *
from math import *

def Primzahlen(anfang,ende):
    [print(x) for x in range(anfang,ende) if istPrimzahl(x)]
        
def istPrimzahl(zahl):
    list_taboo_digits=["0", "2", "4", "5", "6", "8"]
    if zahl < 2 or str(zahl)[0] in list_taboo_digits:
        return False
    for x in range(2, int(sqrt(zahl))):
        if zahl % x == 0:
            return False
    return True
def Primzahlen_Spirale(stelle_primzahlen):
    radians()
    hideturtle()
    speed(10)
    screensize(1920,1080)
    for zahl in range(1, stelle_primzahlen):
        if istPrimzahl(0, zahl) == True:
            penup()
            left(1)
            forward(zahl*1.5)
            pendown()
            circle(2.5)
            penup()
            backward(zahl*1.5)
def Spirale(stelle):
    for zahl in range(1, stelle):
        radians()
        penup()
        left(1)
        forward(zahl*1.5)
        pendown()
        circle(2.5)
        penup()
        backward(zahl*1.5)
            
istPrimzahl(2)
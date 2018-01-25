# Programmer: Bin Xu
# Class: Cpts 111
# Programming Assignment: Project 1 , #1
# Filename: lawOfMotion.py
# Date Created: 25/01/10
# Description:  A program to find an applied force of an object on its mass and acceleration

def LawOfMotion ():
    mass=input ("Enter the mass of object:")
    print mass,"Kg"
    acceleration= input ("Enter the acceleration of object:")
    print acceleration,"m/s^2"
    F= mass* acceleration
    print "applied force=",F,"N"

LawOfMotion ()

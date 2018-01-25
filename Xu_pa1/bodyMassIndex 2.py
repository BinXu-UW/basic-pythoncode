# Programmer: Bin Xu
# Class: Cpts 111
# Programming Assignment: Project 1 , #2
# Filename: bodyMassIndex.py
# Date Created: 25/01/10
# Description: A program that to find a person's body mass index

def bodyMassIndex():
    weight=input ("Enter bodymass in pounds:")
    height=input ("Enter bodyheigt in feet:")
    inches=height*12
    BWI=(weight*703)/(inches*inches)
    print ("BWI=",BWI)

bodyMassIndex()

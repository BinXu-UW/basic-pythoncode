# Programmer: Bin Xu
# Class: Cpts 111  Section 01
# Programming Assignment: Project 02
# Filename: triangle.py  
# Date Created: 02/01/01
# Description: A program that calculates the area of a triangle given the length of its three sides a, b, and c.

import math
def main ():
    a=input ("Enter the length of one of the three sides: ")
    b=input ("Enter the length of one of the three sides: ")
    c=input ("Enter the length of one of the three sides: ")
    s=(a+b+c)/2.0
    A=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print "The area of the triangle is", A

main()
    

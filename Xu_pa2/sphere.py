# Programmer: Bin Xu
# Class: Cpts 111  Section 01
# Programming Assignment: Project 02
# Filename: sphere.py 
# Date Created: 02/01/01
# Description: A program that calculates the volume and surface area of a sphere from its radius

import math
def main():
    r= input ("Enter the radius: ")
    V = (4.0/3.0)*math.pi*(r**3)
    A = 4.0*math.pi*(r**2)
    print "Volume:",V
    print "Surface area:",A

main()



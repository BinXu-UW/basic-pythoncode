# Programmer: Bin Xu
# Class: Cpts 111  Section 01
# Programming Assignment: Project 02
# Filename: slope.py  
# Date Created: 02/01/01
# Description: A program that calculates the slope of a line through two (non-vertical) points entered by the user

def main():
    x1=input ("Enter the first X-axis value X1: ")
    y1=input ("Enter the first Y-axis value Y1: ")
    x2=input ("Enter the second X-axis value X2: ")
    y2=input ("Enter the second Y-axis value Y2: ")
    print "Sloe is ",(y2-y1)/(x2-x1)

main()

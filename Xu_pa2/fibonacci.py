# Programmer: Bin Xu
# Class: Cpts 111  Section 01
# Programming Assignment: Project 02
# Filename: fibonacci.py  
# Date Created: 02/01/01
# Description: A program that computes the nth Fibonacci number where n is a value input by the user

import math
def main():
    u=(1+math.sqrt(5))/2
    v=(1-math.sqrt(5))/2
    n=int (raw_input ("Enter the nth Fibonacci number: "))
    print "The result:", (((1+math.sqrt(5))/2)**n-((1-math.sqrt(5))/2)**n)/(math.sqrt(5))

main()    

    

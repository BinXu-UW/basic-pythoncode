# Programmer: Bin Xu
# Class: Cpts 111  Section 01
# Programming Assignment: Project 02
# Filename: piApproximation.py   
# Date Created: 02/01/01
# Description: A program that calculates the value of ¦Ð by summing the terms of this series: 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ... The program should prompt the user for n, the number of terms to sum, and then output the sum of the first n terms of the series.

import math
temp = int(raw_input("Please input number "));

def add(arg_temp):
    result = 0;
    for i in range(1, arg_temp+1):
        result += 4.0*(((float)((-1)**(i+1)))/((2*i)-1))
    return result

print add(temp)
print "The difference value between approximation and actual vaue of ¦Ð:", math.pi-add(temp)

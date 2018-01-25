# Class: Cpts 111_01
# Programming Assignment: Assignment 6
# Filename: prime.py
# Date Created: 4/7/2010
# Description:A positive whole number n > 2 is prime if no number between 2
#             and ¡Ìn (inclusive) evenly divides n. Write a program that
#             accepts a value of n as input and finds and prints out every
#             prime number less than or equal to n.


import sys
import math

# Programmer: BX
# Class: CptS 111
# Function Name: isPrime()
# Date Created: 4/7/2010
# Description: This function decide the prime number
# Parameters: num is the user input
# Preconditions: 
# Postconditions:
def isPrime(num):
    if not isinstance(num, int):
       return False
    newnum = num
    if newnum < 0:
       newnum = math.fabs(newnum)
    if newnum == 1:
       return False
    if newnum == 2 or newnum == 3:
       return True
    if math.fmod(newnum, 2) == 0:
       return False
    endN = math.sqrt(newnum) + 1 
    i = 3 
    ret = True
    while i < endN: 
       if math.fmod(newnum, i) == 0:
          ret = False
          break;
       i += 2
    return ret


# Programmer: BX
# Class: CptS 111
# Function Name: user_input()
# Date Created: 4/7/2010
# Description: This function let user give a number
# Parameters: 
# Preconditions: 
# Postconditions:
def user_input():
    return int(raw_input("please input a int number: "))


# Programmer: BX
# Class: CptS 111
# Function Name: main()
# Date Created: 4/7/2010
# Description: This function drives the prime program
# Parameters: 
# Preconditions: 
# Postconditions:
def main():
    input = user_input()
    list_result = [1,2,]
    for i in range(3, input+1):
        try:
            if(isPrime(i)):
                list_result.append(i)
            else :
                pass
        except ValueError:
            pass
    return list_result

print main()

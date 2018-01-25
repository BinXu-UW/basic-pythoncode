# Programmer:Bin XU
# Class: Cpts 111_01
# Programming Assignment: Assignment 6
# Filename: Syracuse sequence.py
# Date Created: 4/7/2010
# Description: This program find out the syracuse sequence by using the given
#              formulas, print out the Syracuse sequence for that starting value


# Programmer: BX
# Class: CptS 111
# Function Name: accept_input()
# Date Created: 4/7/2010
# Description: This function let user give a starting value
# Parameters: the starting value is the input
# Preconditions: 
# Postconditions: return the user input

def accept_input():
    user_input = int(raw_input("Please input a natural number:"))
    return user_input


# Programmer: BX
# Class: CptS 111
# Function Name: syracuse()
# Date Created: 4/7/2010
# Description: This function provide the formuals to calculate the ayracuse number
# Parameters: the starting value is the number
# Preconditions: 
# Postconditions:return the ayracuse number

def syracuse(number):
    while number !=1:
        print number,
        if(number%2==0):
            number=number/2
            
        else:
            number=number*3+1
    return number

# Programmer: BX
# Class: CptS 111
# Function Name: main()
# Date Created: 4/7/2010
# Description: This function drives the Syracuse sequence program
# Parameters: 
# Preconditions: 
# Postconditions:

def main ():
    user_input=accept_input()
    print syracuse(user_input)
main ()

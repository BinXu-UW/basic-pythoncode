# Programmer:Bin XU
# Class: Cpts 111_01
# Programming Assignment: Assignment 5
# Filename: grade.py
# Date Created: 3/23/2010
# Description: This program accepts an exam score as input and uses a decision
#              structure to calculate the corresponding grade.



# Programmer: BX
# Class: CptS 111
# Function Name: grade_number()
# Date Created: 3/23/2010
# Description: This function set the numerical grade as input
# Parameters: The input is a integer number from 0 to 100
# Preconditions: Enter a numerical grade as the input
# Postconditions: Return the input

def grade_number():
    number=input ("Enter the numerical grade(0-100):")
    return number

# Programmer: BX
# Class: CptS 111
# Function Name: calculate_letter_grade()
# Date Created: 3/23/2010
# Description: This function calculate the corresponding grade with the grade scale
# Parameters: scale comes from the numerical grade
# Preconditions: 
# Postconditions: 

def calculate_letter_grade(scale):
    if scale<=100 and scale>=90:
        letter_grade='A'
    elif scale<=89 and scale>=80:
        letter_grade='B'
    elif scale<=79 and scale>=70:
        letter_grade='C'
    elif scale<=69 and scale>=60:
        letter_grade='D'
    elif scale<60:
        letter_grade='F'
    
    return letter_grade

# Programmer: BX
# Class: CptS 111
# Function Name: main()
# Date Created: 3/23/2010
# Description: This function drives the grade program
# Parameters: 
# Preconditions: 
# Postconditions: 
def main():
    letter_grade=calculate_letter_grade(grade_number())
    print "letter grade:", letter_grade

main()

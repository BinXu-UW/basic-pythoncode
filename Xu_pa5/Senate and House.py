# Programmer:Bin XU
# Class: Cpts 111_01
# Programming Assignment: Assignment 5
# Filename: Senate and House.py
# Date Created: 3/23/2010
# Description: This problem will determine a person whether or not has 
#              eligibility for the Senate and House based on his age and
#              the years of citizenship


# Programmer: BX
# Class: CptS 111
# Function Name: def Age()
# Date Created: 3/23/2010
# Description: This function set the age as a input
# Parameters: The input is a integer number 
# Preconditions: Enter a age as the input
# Postconditions: Return the input

def Age():
    age = int(raw_input('Enter a age: '))
    return age


# Programmer: BX
# Class: CptS 111
# Function Name: years_of_citizenship()
# Date Created: 3/23/2010
# Description: This function set the years of citizenship as ainput
# Parameters: The input is a integer number 
# Preconditions: Enter the years of citizenship as the input
# Postconditions: Return the input

def years_of_citizenship():
    years_of_citizenship = int(raw_input('Enter years of citizenship: '))
    return years_of_citizenship
   


# Programmer: BX
# Class: CptS 111
# Function Name: evaluation()
# Date Created: 3/23/2010
# Description: This function evaluation the corresponding job with the age and years of citizenship
# Parameters: age and years of citizenship come from Age() and years_of_citizenship()
# Preconditions: 
# Postconditions:         
def evaluation(age,years_of_citizenship):
    if age >= 30 and years_of_citizenship >= 9:
        result = 'This person has the eligibility to be a US senator or a US representative '
    elif age >= 25 and years_of_citizenship >= 7 :
        result = "This person just has the eligibility to be a US representative "
    else :
        result = " Sorry, this person dose not has the eligibilitye to be a US senator or a US representative "

    return result

# Programmer: BX
# Class: CptS 111
# Function Name: main()
# Date Created: 3/23/2010
# Description: This function drives the Senate and House program
# Parameters: 
# Preconditions: 
# Postconditions: 
def main():
    result = evaluation(Age(),years_of_citizenship())
    print result
    
main()    

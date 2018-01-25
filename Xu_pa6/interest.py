# Programmer:Bin XU
# Class: Cpts 111_01
# Programming Assignment: Assignment 6
# Filename: interest.py
# Date Created: 4/7/2010
# Description: This program accepts an interest rate as input and uses a
#              while loop decision to calculate the number of years it takes an
#              investment to duble
            

# Programmer: BX
# Class: CptS 111
# Function Name: interest_rate()
# Date Created: 4/7/2010
# Description: This function set the interest rate as input
# Parameters: rate from the user input
# Preconditions: 
# Postconditions:return years

def interest_rate(rate):
    years=1
    while ((1+rate)**years <2):
        years=years+1
    return years

# Programmer: BX
# Class: CptS 111
# Function Name: main()
# Date Created: 4/7/2010
# Description: This function drives the interest program
# Parameters: 
# Preconditions: 
# Postconditions:
def main( ):
    rate=input("Enter the interest rate : ")
    years=interest_rate(rate)
    print years, "years"
main()

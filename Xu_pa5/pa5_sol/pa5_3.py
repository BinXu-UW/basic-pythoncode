# Programmer: Andrew S. O'Fallon
# Class: CptS 111
# Programming Assignment: 5 KEY - Problem 3
# Filename: pa5_2.py
# Date Created: March 7, 2010
# Description:

# Programmer: AO
# Class: CptS 111
# Function Name: 
# Date Created: 
# Description: 
# Parameters: 
# Preconditions: 
# Postconditions:

def get_age():
    age = raw_input("Please enter age: ")
    age = int(age)

    return age

# Programmer: AO
# Class: CptS 111
# Function Name: 
# Date Created: 
# Description: 
# Parameters: 
# Preconditions: 
# Postconditions:

def get_years_citizenship():
    years = raw_input("Please enter number of years as US citizen: ")
    years = int(years)

    return years

# Programmer: AO
# Class: CptS 111
# Function Name: 
# Date Created: 
# Description: 
# Parameters: 
# Preconditions: 
# Postconditions:

def is_eligible_senate(age, years_citizenship):
    # 1 means eligible for senate; 0 not eligible
    status = 0
    # A person is eligible to be a US senator
    # if they are at least 30 years old and have been a
    # US citizen for at least 9 years
    if age >= 30 and years_citizenship >= 9:
        status = 1

    return status

# Programmer: AO
# Class: CptS 111
# Function Name: 
# Date Created: 
# Description: 
# Parameters: 
# Preconditions: 
# Postconditions:

def is_eligible_house(age, years_citizenship):
    # 1 means eligible for house; 0 not eligible
    status = 0
    # A person is eligible to be a house rep
    # if they are at least 25 years old and have been a
    # US citizen for at least 7 years
    if age >= 25 and years_citizenship >= 7:
        status = 1

    return status
    
# Programmer: AO
# Class: CptS 111
# Function Name: 
# Date Created: 
# Description: 
# Parameters: 
# Preconditions: 
# Postconditions:

def print_eligibility(senate_status, house_status):
    if senate_status == 1:
        print "Eligible for senate seat!"
    else:
        print "Not eligible for senate seat!"

    if house_status == 1:
        print "Eligible for house seat!"
    else:
        print "Not eligible for house seat!"

# Programmer: AO
# Class: CptS 111
# Function Name: main()
# Date Created: 
# Description: 
# Parameters: 
# Preconditions: 
# Postconditions:

def main():
    age = get_age()
    years_citizenship = get_years_citizenship()
    senate_status = is_eligible_senate(age, years_citizenship)
    house_status = is_eligible_house(age, years_citizenship)
    print_eligibility(senate_status, house_status)
    
main()

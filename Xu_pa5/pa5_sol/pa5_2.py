# Programmer: Andrew S. O'Fallon
# Class: CptS 111
# Programming Assignment: 5 KEY - Problem 2
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

def open_file(filename, mode):
    infile = open(filename, mode)

    return infile

# Programmer: AO
# Class: CptS 111
# Function Name: 
# Date Created: 
# Description: 
# Parameters: 
# Preconditions: 
# Postconditions:

def get_year(infile):
    # Read in year as text
    year = infile.readline()

    return year

# Programmer: AO
# Class: CptS 111
# Function Name: 
# Date Created: 
# Description: 
# Parameters: 
# Preconditions: 
# Postconditions:

def is_leap_year(year):
    # We will assume that year is not a leap year be default 0 means not a leap year;
    # 1 means the year is a leap year
    status = 0

    # Remember: A year is a leap year if it is divisible by 4,
    # unless it is a century year that is not divisible by 400.
    if (year % 4) == 0:
        status = 1
        if (year % 100) == 0:
            status = 0
            if (year % 400) == 0:
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

def print_leap_year_status(year, status):
    if status == 1:
        print "Year", year, "is a leap year!"
    else:
        print "Year", year, "is NOT a leap year!"

# Programmer: AO
# Class: CptS 111
# Function Name: main()
# Date Created: 
# Description: 
# Parameters: 
# Preconditions: 
# Postconditions:

def main():
    infile = open_file("years.txt", "r")

    year = get_year(infile)
    while year != "": # Keep getting years until we are at the end of the file
        # Convert text year to integer year
        year = int(year)
        status = is_leap_year(year)
        print_leap_year_status(year, status)
        year = get_year(infile)
    
main()

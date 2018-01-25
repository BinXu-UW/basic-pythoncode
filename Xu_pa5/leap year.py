# Programmer:Bin XU
# Class: Cpts 111_01
# Programming Assignment: Assignment 5
# Filename: leap year.py
# Date Created: 3/24/2010
# Description: This program accepts years as input and uses a decision
#              structure to determine whether or not they are leap year.

import string



# Programmer:Bin XU
# Class: Cpts 111_01
# Programming Assignment: Assignment 5
# Function Name:open_file()
# Date Created: 3/24/2010
# Description: This function open file 
# Parameters: filename and mode
# Preconditions: 
# Postconditions: 
def open_file(filename, mode):
       file_handle = file(filename, mode)
       return file_handle

# Programmer:Bin XU
# Class: Cpts 111_01
# Programming Assignment: Assignment 5
# Function Name:close_file()
# Date Created: 3/24/2010
# Description: This function close file 
# Parameters: 
# Preconditions: 
# Postconditions: 
def close_file(file_handle):
    file_handle.close()


# Programmer:Bin XU
# Class: Cpts 111_01
# Programming Assignment: Assignment 5
# Function Name:get_string()
# Date Created: 3/24/2010
# Description: This function get string and make the years become a list 
# Parameters: year string from the file
# Preconditions: 
# Postconditions:
def get_string(file_handle):
    list_test = [];
    while(1):
        year_string = file_handle.readline()
        if len(year_string) == 0:
            break;
        list_test.append(year_string);
    return list_test;

# Programmer:Bin XU
# Class: Cpts 111_01
# Programming Assignment: Assignment 5
# Function Name:convert_integer()
# Date Created: 3/24/2010
# Description: This function convert a year into a integer
# Parameters: year string from the list
# Preconditions: 
# Postconditions:
def convert_integer(year_string):
    year= int(year_string)
    return year

# Programmer:Bin XU
# Class: Cpts 111_01
# Programming Assignment: Assignment 5
# Function Name:calculate()
# Date Created: 3/24/2010
# Description: This function determine the leap year
# Parameters: 
# Preconditions: 
# Postconditions:
def calculate(year):
    if (year%4==0 and year%100!=0)or(year%400==0):
        output="This year is a leap year"
    else:
        output="This year is not a leap year"
    return output
# Programmer: BX
# Class: CptS 111
# Function Name: main()
# Date Created: 3/24/2010
# Description: This function drives the leap year program
# Parameters: 
# Preconditions: 
# Postconditions: 
def main():
    year_string = [];
    file_handle = open_file("years.txt","r")
    year_string = get_string(file_handle)
    for i in range(0,len(year_string)):
        year= convert_integer(year_string[i])
        print year;
        print calculate(year)
    close_file(file_handle)

main()

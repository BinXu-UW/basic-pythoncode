# Programmer: Andrew S. O'Fallon
# Class: CptS 111
# Programming Assignment: 5 KEY - Problem 1
# Filename: pa5_1.py
# Date Created: March 7, 2010
# Description:

# Programmer: AO
# Class: CptS 111
# Function Name: get_exam_score()
# Date Created: 
# Description: 
# Parameters: 
# Preconditions: 
# Postconditions: 

def get_exam_score():
    exam_score = raw_input("Please enter the exam score: ")
    exam_score = float(exam_score)

    return exam_score

# Programmer: AO
# Class: CptS 111
# Function Name: determine_letter_grade()
# Date Created: 
# Description: 
# Parameters: 
# Preconditions: 
# Postconditions:

def determine_letter_grade(exam_score):
    if exam_score >= 90.0:
        letter_grade = 'A'
    elif exam_score >= 80.0:
        letter_grade = 'B'
    elif exam_score >= 70.0:
        letter_grade = 'C'
    elif exam_score >= 60.0:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    return letter_grade

# Programmer: AO
# Class: CptS 111
# Function Name: print_letter_grade()
# Date Created: 
# Description: 
# Parameters: 
# Preconditions: 
# Postconditions:

def print_letter_grade(exam_score, letter_grade):
    print "An exam score of", exam_score, "is a(n)", letter_grade

# Programmer: AO
# Class: CptS 111
# Function Name: main()
# Date Created: 
# Description: 
# Parameters: 
# Preconditions: 
# Postconditions:

def main():
    exam_score = get_exam_score()
    letter_grade = determine_letter_grade(exam_score)
    print_letter_grade(exam_score, letter_grade)

main()

# Video Store Fee System

# This example illustrates how to perform conversions between different types.
# The problem is to calculate the late fee owed by a person for a single
# video rental. The person is charged $2.00 for the first day late and
# $0.50 for each additional date late. Fractions of a day must be rounded
# to the smallest integer that is greater than that number.

# General algorithm
# 1. Get the number of days late from the user
# 2. Compute the late fee according to the number of days late
# 3. Display the late fee

import math

def main ():
    days_late = input("Please enter the number of days late: ")

    # Does Solution 1 have any precision problems? Do we always obtain the same result
    # as with Solution 2?
    # money_owed = 2.0 + (int(days_late + 0.9999) * 0.5) - 0.5 # Solution 1
    money_owed = 2.0 + 0.5 * (math.ceil(days_late) - 1.0) # Solution 2
    
    print "Late fee:", money_owed
    
main ()

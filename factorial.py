# Factorial - This program computes the factorial of the number enter by
#             the user and displays the result.

# Required algorithm
# 1. Get the value for n from the user
# 2. Compute n!
# 3. Display the result of n!

def main ():
    n = 0 # Initialize our variables
    factorial = 1

    n = input ("Enter a term: ")

    # Please focus on what we have done with the range function.
    # We are counting down from n.
    for i in range (n, 1, -1):
        factorial = factorial * i

    # Do we have limitations on the largest value that we can compute with
    # a 32-bit integer? Yes, 2^32 - 1 is the largest number that can be
    # stored in a 32-bit integer. Please consider how Python handles these
    # limitations...long integers!
    print "Factorial of", n, "is", factorial

main ()

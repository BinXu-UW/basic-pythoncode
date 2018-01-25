# This example illustrates how to perform type conversions between
# integers and floats. Recall that when we have mixed types, i.e. floats
# and integers in a single expression, the expression is always evaluated
# to the more concise type. In this case, float.

def main ():
    num_scores = 3
    
    score1 = raw_input("Enter score1: ")
    score2 = raw_input("Enter score2: ")
    score3 = raw_input("Enter score3: ")

    float_score1 = float(score1)

    sum_result = float(score1) + float(score2) + float(score3)

    # The below average score calculation is commented
    # out because the float () type conversion is placed incorrectly. Why?
    # Well, we are possibly still performing integer division between
    # sum_result and num_scores and thus will convert the integer
    # result to a float...we do not want this result.
    # average_score = float(sum_result / num_scores)

    # This is the correct method for converting types. We are ensuring
    # that at least the sum_result is a float. When we have mixed types
    # i.e. float / int we obtain a float back. Thus, average_score
    # will contain a very precise result.
    average_score = float(sum_result) / num_scores

    print ("Average:", average_score)

main ()

import math

def main():
    
    n=int (raw_input ("Enter the nth Fibonacci number: "))
    print "The result:", (((1+math.sqrt(5))/2)**n-((1-math.sqrt(5))/2)**n)/(math.sqrt(5))

main()

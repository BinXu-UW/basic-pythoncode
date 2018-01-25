# Programmer: Bin Xu
# Class: Cpts 111
# Programming Assignment: Project 1 , #4
# Filename: investments.py
# Date Created: 25/01/10
# Description: A that determines the vale of an investment some number of years in the future.


def Invest():
    principal = input("Principal:")
    apr = input("Annual Percentage Rate:")
    years = input("Number of years to invest:")


    for count in range(years):
        principal = principal * (1 + apr)
    print "principal=", principal
    
Invest()

# Programmer: Bin Xu
# Class: Cpts 111
# Programming Assignment: Project 1 , #2
# Filename: fahrenheitToCelsius.py
# Date Created: 25/01/10
# Description: A program that performs 5 different conversions of temperatures provided in degrees Fahrenheit to degrees Celsius.

def fahrenheitToCelsius():
    fahrenheit1=input ("Enter Fahrenheit temperature1:") 
    fahrenheit2=input ("Enter Fahrenheit temperature2:")
    fahrenheit3=input ("Enter Fahrenheit temperature3:")
    fahrenheit4=input ("Enter Fahrenheit temperature4:")
    fahrenheit5=input ("Enter Fahrenheit temperature5:")
    celsius1 = (fahrenheit1 - 32.0) * 5.0/9.0
    celsius2 = (fahrenheit2 - 32.0) * 5.0/9.0
    celsius3 = (fahrenheit3 - 32.0) * 5.0/9.0
    celsius4 = (fahrenheit4 - 32.0) * 5.0/9.0
    celsius5 = (fahrenheit5 - 32.0) * 5.0/9.0
    
    
    print ("Celsius Temperature1=",celsius1)
    print ("Celsius Temperature2=",celsius2)
    print ("Celsius Temperature3=",celsius3)
    print ("Celsius Temperature4=",celsius4)
    print ("Celsius Temperature5=",celsius5)
       
       

fahrenheitToCelsius()


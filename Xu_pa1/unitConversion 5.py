# Programmer: Bin Xu
# Class: Cpts 111
# Programming Assignment: Project 1 , #1
# Filename: unitConversion.py
# Date Created: 25/01/10
# Description:A program that performs a unit conversion.

def conversion():
    km=input ("1. Enter kilometers:")
    mile=km*0.621
    print "Result:",mile,"mile"
    m=input ("2. Enter meters:")
    feet=m*3.281
    print "Result:",feet,"ft"
    cm=input ("3. Enter centimetres:")
    inch=cm*0.394
    print "Result:",inch,"in"
    skm=input("4. Enter square kilometres:")
    hectare=skm*100
    print "Result:",hectare,"ha"
    sm=input("5. Enter square metres:")
    square_foot=sm*10.764
    print "Result:",square_foot,"ft^2"
    cubic_meter=input ("6. Enter cubic meters:")
    liter=cubic_meter*1000
    print "Result:",liter,"liter"
    gallon=input("7. Enter gallons:")
    pint=gallon*0.946/0.473
    print "Result:",pint,"pt"
    ton=input("8. Enter tons:")
    pound=ton*2205
    print "Result:",pound,"lb"
    ounce=input("9. Enter ounces:")
    gram=ounce*28.350
    print "Result:",gram,"g"
    N=input ("10. Enter newton:")
    Lbf=N*0.225
    print "Result:",Lbf,"lbf"
    
    

conversion()


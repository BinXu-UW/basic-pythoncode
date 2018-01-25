def operation(celsius):
    print (celsius - 32.0) * 5.0/9.0;

def inputnumber():
    for i in range(1,6):
        operation(input ("Enter Fahrenheit temperature1:"));
        
inputnumber(); 

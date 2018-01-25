import string

def checksum(message):
    
    for line in message:
        
        a = len(line)
        sum_message = 0
        for i in range(a):
            
            if ord(line[i]) !=46:
                sum_message = sum_message + ord(line[i])
            if ord(line[i]) ==46:
                checksum = sum_message % 64            
                checksumcharactor = chr(checksum)
                
                
                if sum_message !=0:
                    print checksumcharactor,"\n"
                if sum_message ==0:
                    print "Done"
                sum_message = 0
                                                
                                            

def readline(inputData):
     message = inputData.readlines()
     return message


def main():
    inputData = open("input.txt","r")
    message = readline(inputData)
    checksum(message)


main()

# Programmer: Bin XU
# Class:Cpts 111_01
# Programming Assignment: Assignment 3
# Filename:Caesar Cipher
# Date Created:2/24/2010
# Description:Write a program that can encode and decode Caesar ciphers.
#             The program should prompt the user to enter 1 to encode a
#             message and 2 to decode a message.




import string
class Caesar_Cipher:
    def __init__(self):
        message = raw_input("Enter the message :")
        f_message = file('message.txt', 'w')
        f_message.write(message)
        
    def encode(self, onelinemessage, step):
        list_encoderesult = []
        step = step
        for i in range(0, len(onelinemessage)):
            m_number = ord(onelinemessage[i])
            print m_number
            if((0 == i)&(m_number <97)&(m_number != 10)&(m_number!=13)&(m_number!=32)):
                step = int(chr(m_number))
            if((m_number !=32)&(m_number!= 10)&(m_number!=13)&(m_number>=97)):
                m_number+=step
                if(m_number>122):
                    m2_number = m_number-122
                    m_number = m2_number + 97 -1
            print m_number
            m2_number = chr(m_number)
            print m2_number
            list_encoderesult.append(m2_number)
        return list_encoderesult

    def decode(self, onelinemessage, step):
        list_decoderesult = []
        step = step
        for i in range(0, len(onelinemessage)):
            m_number = ord(onelinemessage[i])
            print m_number
            if((m_number==10)|(m_number==13)|(m_number==32)|(m_number <=57)):
                pass
            else:
                m_number-=step
                if(m_number<97):
                    m2_number = 97-m_number
                    m_number = 122+ 1 - m2_number
            print m_number
            m2_number = chr(m_number)
            print m2_number
            list_decoderesult.append(m2_number)
        return list_decoderesult


def readtext():
    print "****************************Assignment 3********************"
    print "function: encode and decode                              "
    print "1: encode                                                "
    print "2: decode                                                "
    print "The format of the message should be like '3secret', '3' is the shift value."
    print "letters should be lowercase."
    print "### After the program is complete, please check the plaintext.txt to get the decoded message!"
    print "                                                         "
    
    filecontent = Caesar_Cipher()
    file_read = file('message.txt', 'r')
    file_plain= file('plaintext.txt',  'a+')
    file_cipher= file('ciphertext.txt',  'w')
    command = True
    x = 0
    step = 0
    while(command):
        user_input = int(raw_input("please input 1 first then 2  >>> "))
        if(user_input == 1):
            while(True):
                line =file_read.readline()
                print "user input:",line
                if(len(line) == 0):
                    break
                if(x == 0):
                    print "check #1"
                    fe = filecontent.encode(line, 0)
                    fe_number = ord(fe[0])
                    step = int(chr(fe_number))
                    print "step is ", step
                    x+=1
                    print "check #2", x
                else:
                    print "check #3", step
                    fe = filecontent.encode(line, step)
                message_join = string.join(fe, '')
                file_plain.write(message_join)
        elif(user_input == 2):
            file_plain = file('plaintext.txt',  'a+')
            while(True):
                line =file_plain.readline()
                if(len(line) == 0):
                    break
                fe = filecontent.decode(line, step)
                message_join = string.join(fe, '')
                file_cipher .write(message_join)
                command = False
        file_read.close()
        file_plain.close()
    file_cipher.close()

readtext()


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
                    bb = m_number-122
                    m_number = bb + 97 -1
            print m_number
            bb = chr(m_number)
            print bb
            list_encoderesult.append(bb)
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
                    bb = 97-m_number
                    m_number = 123 - bb
            print m_number
            bb = chr(m_number)
            print bb
            list_decoderesult.append(bb)
        return list_decoderesult


def readtext():
    print "****************************Assignment 3********************"
    print "function: encode and decode                              "
    print "1: encode                                                "
    print "2: decode                                                "
    print "The format of the message should be like '3secret', '3' is the shift value."
    print "letters should be lowercase."
    print "                                                         "
    
    filecontent = Caesar_Cipher()
    f_read = file('message.txt', 'r')
    f = file('ciphertext.txt',  'a+')
    ff = file('plaintext.txt',  'w')
    flag = True
    i = 0
    step = 0
    while(flag):
        user_input = int(raw_input("please input 1 first then 2  >>> "))
        if(user_input == 1):
            while(True):
                line =f_read.readline()
                print "user input:",line
                if(len(line) == 0):
                    break
                if(i == 0):
                    print "xxxxxxxxxxxxxxx"
                    vv = filecontent.encode(line, 0)
                    xx = ord(vv[0])
                    step = int(chr(xx))
                    print "step is ", step
                    i+=1
                    print "vvvvvvvvvvvvv", i
                else:
                    print "ssssssssssssss", step
                    vv = filecontent.encode(line, step)
                ss = string.join(vv, '')
                f.write(ss)
        elif(user_input == 2):
            f = file('ciphertext.txt',  'a+')
            while(True):
                line =f.readline()
                if(len(line) == 0):
                    break
                vv = filecontent.decode(line, step)
                ss = string.join(vv, '')
                ff.write(ss)
                flag = False
        f_read.close()
        f.close()
    ff.close()

readtext()


# Class:Cpts 111_01
# Programming Assignment: Assignment 4
# Filename:Caesar Cipher
# Date Created:3/10/2010
# Description:Write a program that can encode and decode Caesar ciphers.Functional
#             decomposition provides a way to split your original program into
#             multiple functions.You may recall that we have discussed several
#             reasons as to why you should break your program into multiple
#             functions that solve a sub-problem.




import string

#This function opens a file with name filename for mode,where mode must
#be "r" or "w".This function returns the handle to the file.
def open_file(filename, mode):
    f = file(filename, mode);
    return f

# This function closes the file pointed to by file_handle.
def close_file(file_handle):
    file_handle.close()
    
#This function reads the plaintext or ciphertext string from the file handled
#by file_handle and returns the string.
def get_string(file_handle):
    while(True):
        line = file_handle.readline();
        if(len(line) == 0):
            break;
        return line
    
#This function outputs or writes the plaintext or ciphertext string stored in
#text_string to the file handled by file_handle.
def write_string(file_handle, text_string):
    file_handle.write(text_string)
    
#This function encodes the plaintext_string using the Caesar cipher and returns
#the encoded string.
def encode_message(plaintext_string):
    shift_key = int(plaintext_string[0])
    ciphertext_string = plaintext_string[0]
    for index in range(1, len(plaintext_string) ):
        if plaintext_string[index] == ' ':
            ciphertext_string = ciphertext_string + ' '
        else:
            plaintext_string = string.lower(plaintext_string)
            alpha_char_position = (ord(plaintext_string[index]) - 97)
            encoded_char_position = alpha_char_position + shift_key
            if encoded_char_position > 26:
               encoded_char_position = encoded_char_position - 26
            else:
                encoded_char_position = encoded_char_position
            encoded_char = chr(encoded_char_position + 97 )
            ciphertext_string = ciphertext_string + encoded_char

    return ciphertext_string

#This function decodes the ciphertext_string using and returns the decoded string.
def decode_message(ciphertext_string):
    shift_key = int(ciphertext_string[0])
    plaintext_string = ciphertext_string[0]
    for index in range(1, len(ciphertext_string) ):
        if ciphertext_string[index] == ' ':
            plaintext_string = plaintext_string + ' '
        else:
            ciphertext_string = string.lower(ciphertext_string)
            alpha_char_position = (ord(ciphertext_string[index]) - 97)
            decode_char_position = alpha_char_position - shift_key
            if decode_char_position < 0:
                decode_char_position = decode_char_position + 26
            else:
                decode_char_position = decode_char_position
            decode_char = chr(decode_char_position + 97 )
            plaintext_string = plaintext_string + decode_char
    return  plaintext_string

#This function needs to drive the Caesar cipher program so that the appropriate
#function calls are made in the appropriate order.
def main():
    option = int(raw_input('Enter 1 to encode a message and 2 to decode a message: '))
    if option == 1:
        #read plaintext, then start decode and write result
        infile = open_file("plaintext.txt","r")
        get_string_infor= get_string(infile)
        close_file(infile)
        ciphertext_string = encode_message(get_string_infor)
        #record encode result
        outfile = open_file("ciphertext.txt","w")
        write_string(outfile, ciphertext_string)
        close_file(outfile)
        
    elif option == 2:
         #read ciphertext, then start encode and write result
         infile = open_file("ciphertext.txt","r")
         get_string_infor= get_string(infile)
         close_file(infile)
         plaintext_string = decode_message(get_string_infor)
         #record decode result
         outfile = open_file("plaintext.txt","w")
         write_string(outfile, plaintext_string)
         close_file(outfile);
         
    else:
        print ("error: you must input 1 or 2\n")

main()

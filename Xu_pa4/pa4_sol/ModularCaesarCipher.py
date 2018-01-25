# Programmer: Andrew S. O'Fallon
# Class: CptS 111
# Programming Assignment: 4 KEY - Computing with Strings (Caesar Cipher)
# Filename: ModularCaesarCipher.py
# Date Created: March 4, 2010
# Description: This program encodes and decodes Caesar cipher messages.
#              This program also emphasizes a modular approach to the
#              Caesar Cipher problem.

import string

# Programmer: AO
# Class: CptS 111
# Function Name: open_file()
# Date Created: March 4, 2010
# Description: This function opens a file for read or write mode
# Parameters: filename a string, mode a string
# Preconditions: Must know the filename and mode
# Postconditions: File has been opened

def open_file(filename, mode):
    file_handle = open(filename, mode)

    return file_handle

# Programmer: AO
# Class: CptS 111
# Function Name: close_file()
# Date Created: March 4, 2010
# Description: This function closes a file
# Parameters: The file handle to the file to close
# Preconditions: File must be opened already
# Postconditions: File will be closed

def close_file(file_handle):
    file_handle.close()

# Programmer: AO
# Class: CptS 111
# Function Name: get_string()
# Date Created: March 4, 2010
# Description: This function gets a single string from a file
# Parameters: The handle to the file that is to be read from
# Preconditions: A file has been opened for read
# Postconditions: A single string from a file has been read

def get_string(file_handle):
    text_string = file_handle.readline()

    return text_string
    
# Programmer: AO
# Class: CptS 111
# Function Name: write_string()
# Date Created: March 4, 2010
# Description: This function writes a single string to a file
# Parameters: The file handle to the output file, the string to be written
# Preconditions: An open file, a string
# Postconditions: A string has been written to a file

def write_string(file_handle, text_string):
    file_handle.write(text_string)

# Programmer: AO
# Class: CptS 111
# Function Name: encode_message()
# Date Created: March 4, 2010
# Description: This function encodes a plaintext message into a ciphertext message.
#              Caesar Cipher encoding is used.
# Parameters: The plaintext string
# Preconditions:
# Postconditions:

def encode_message(plaintext_string):
    # We know that the shift key is the first character in the string
    # read from the file. We want to make sure that we manipulate
    # the key as an integer value.
    shift_key = int(plaintext_string[0])
    ciphertext_string = plaintext_string[0]

    # Note that the length of the plaintext string includes the
    # newline character. We want to ignore this character so we
    # only encode the message up to the newline (i.e. len - 1). Also
    # note that we start the range from 1 because we know that index
    # 0 refers to the shift key that we have already gathered from
    # the string.
    for index in range(1, len(plaintext_string) - 1):
        if plaintext_string[index] == ' ':
            ciphertext_string = ciphertext_string + ' '
        else:
            # We want to know the position of the plaintext character
            # relative to the beginning of the alphabet. For example,
            # 'a' == 1, 'b' == 2, 'c' == 3,..., 'z' = 26
            plaintext_string = string.lower(plaintext_string)
            alpha_char_position = (ord(plaintext_string[index]) - ord('a')) + 1
            # Determine the appropriate encoded character. We can rotate
            # from 'z' to 'a' by using the below equation. The remainder operator
            # allows us to before this rotating operation.
            encoded_char_position = (alpha_char_position + shift_key) % 26
            encoded_char = chr(encoded_char_position + ord('a') - 1)
            ciphertext_string = ciphertext_string + encoded_char

    return ciphertext_string

# Programmer: AO
# Class: CptS 111
# Function Name: decode_message()
# Date Created: March 4, 2010
# Description: This function decodes a ciphertext message into a plaintext message.
#              Caesar Cipher decoding is used.
# Parameters: The ciphertext string
# Preconditions:
# Postconditions:

def decode_message(ciphertext_string):
    # We know that the shift key is the first character in the string
    # read from the file. We want to make sure that we manipulate
    # the key as an integer value.
    shift_key = int(ciphertext_string[0])
    plaintext_string = ciphertext_string[0]

    # Note that the length of the ciphertext string includes the
    # newline character. We want to ignore this character so we
    # only decode the message up to the newline (i.e. len - 1). Also
    # note that we start the range from 1 because we know that index
    # 0 refers to the shift key that we have already gathered from
    # the string.
    for index in range(1, len(ciphertext_string) - 1):
        if ciphertext_string[index] == ' ':
            plaintext_string = plaintext_string + ' '
        else:
            # We want to know the position of the ciphertext character
            # relative to the beginning of the alphabet. For example,
            # 'a' == 1, 'b' == 2, 'c' == 3,..., 'z' = 26
            ciphertext_string = string.lower(ciphertext_string)
            alpha_char_position = (ord(ciphertext_string[index]) - ord('a')) + 1
            # Determine the appropriate decoded character. We can rotate
            # from 'a' to 'z' by using the below equation. The remainder operator
            # allows us to before this rotating operation.
            decoded_char_position = alpha_char_position - shift_key
            if decoded_char_position <= 0:
                decoded_char_position = decoded_char_position + 26
            decoded_char = chr(decoded_char_position + ord('a') - 1)
            plaintext_string = plaintext_string + decoded_char

    return plaintext_string

# Programmer: AO
# Class: CptS 111
# Function Name: main()
# Date Created: March 4, 2010
# Description: This function drives the Caesar Cipher program
# Parameters:
# Preconditions:
# Postconditions:

def main():
    option = raw_input("Please enter 1 to encode a message or 2 to decode a message: ")
    # Convert option to an integer
    option = int(option)

    if option == 1: # Convert plaintext to ciphertext
        infile_handle = open_file("plaintext.txt", "r")
        outfile_handle = open_file("ciphertext.txt", "w")

        plaintext_string = get_string(infile_handle)
        print "Plaintext:", plaintext_string

        ciphertext_string = encode_message(plaintext_string)
        print "Ciphertext:", ciphertext_string
        write_string(outfile_handle, ciphertext_string)
        print "SUCCESS: Plaintext to ciphertext conversion complete!"
        
        # Make sure to close your files!
        close_file(infile_handle)
        close_file(outfile_handle)
    elif option == 2: # Convert ciphertext to plaintext
        infile_handle = open_file("ciphertext.txt", "r")
        outfile_handle = open_file("plaintext.txt", "w")
        
        ciphertext_string = get_string(infile_handle)        
        print "Ciphertext:", ciphertext_string
        
        plaintext_string = decode_message(ciphertext_string)
        print "Plaintext:", plaintext_string
        outfile_handle.write(plaintext_string)
        print "SUCCESS: Ciphertext to plaintext conversion complete!"
        
        # Make sure to close your files!
        close_file(infile_handle)
        close_file(outfile_handle)
    else:
        print "ERROR: Invalid entry. Exiting the program!"

main()

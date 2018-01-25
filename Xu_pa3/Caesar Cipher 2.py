import string

def encode_message(plain_string):
    shift_key = int(plain_string[0])
    cipher_string = plain_string[0]
    for index in range(1, len(plain_string) ):
        if plain_string[index] == ' ':
            cipher_string = cipher_string + ' '
        else:
            plain_string = string.lower(plain_string)
            alpha_char_position = (ord(plain_string[index]) - 97)
            encoded_char_position = alpha_char_position + shift_key
            if encoded_char_position > 26:
               encoded_char_position = encoded_char_position - 26
            else:
                encoded_char_position = encoded_char_position
            encoded_char = chr(encoded_char_position + 97 )
            cipher_string = cipher_string + encoded_char

    return cipher_string

def decode_message(cipher_string):
    shift_key = int(cipher_string[0])
    plain_string = cipher_string[0]
    for index in range(1, len(cipher_string) ):
        if cipher_string[index] == ' ':
            plain_string = plain_string + ' '
        else:
            cipher_string = string.lower(cipher_string)
            alpha_char_position = (ord(cipher_string[index]) - 97)
            decode_char_position = alpha_char_position - shift_key
            if decode_char_position < 0:
                decode_char_position = decode_char_position + 26
            else:
                decode_char_position = decode_char_position
            decode_char = chr(decode_char_position + 97 )
            plain_string = plain_string + decode_char
    return  plain_string       
def main():
    option = int(raw_input('Enter 1 to encode a message and 2 to decode a message: '))
    if option == 1:
        infile = open("plaintext.txt","r")
        plain_string = infile.readline()
        cipher_string = encode_message(plain_string)
        outfile = open("ciphertext.txt","w")
        outfile.write(str(cipher_string))
        infile.close()
        outfile.close()
        
    elif option == 2:
         infile = open("ciphertext.txt","r")
         cipher_string = infile.readline()
         plain_string = decode_message(cipher_string)
         outfile = open("plaintext.txt","w")
         outfile.write(str(plain_string))
         infile.close()
         outfile.close()

main()

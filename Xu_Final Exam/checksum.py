def open_file(filename, mode):
    detail = file(filename, mode);
    return detail

def close_file(file_handle):
    file_handle.close()

def get_string(file_handle):
    while(True):
        line = file_handle.readline();
        if(len(line) == 0):
            break;
        print line
        return line

def main():
    infile = open_file("input.txt", "r");
    get_detail = get_string(infile)
    close_file(infile)
    sum = 0;
    for i in get_detail:
        sum+=ord(i)
    print "the checksum is",sum
    print "the remainder is",sum%64
    
    print "the checksumcharacter is",chr(sum%64)


main()

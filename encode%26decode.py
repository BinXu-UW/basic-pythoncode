#encode and decode program
#detail 1:encode; 2:decode
# date: 2/21/10



import string;
class encodeanddecode:
    def __init__(self):
        message = '''\
3secrct
''';
        f_message = file('message.txt', 'w');
        f_message.write(message);

    def __del__(self):
        pass;

    def encode(self, onelinemessage, step):
        list_encoderesult = [];
        step = step;
        for i in range(0, len(onelinemessage)):
            aa = ord(onelinemessage[i]);
            print aa;
            if((0 == i)&(aa <97)&(aa != 10)&(aa!=13)&(aa!=32)):
                step = int(chr(aa));
            if((aa !=32)&(aa!= 10)&(aa!=13)&(aa>=97)):
                aa+=step;
                if(aa>122):
                    bb = aa-122;
                    aa = bb + 97 -1;
            print aa;
            bb = chr(aa);
            print bb;
            list_encoderesult.append(bb);
        return list_encoderesult;

    def decode(self, onelinemessage, step):
        list_decoderesult = [];
        step = step;
        for i in range(0, len(onelinemessage)):
            aa = ord(onelinemessage[i]);
            print aa;
            if((aa==10)|(aa==13)|(aa==32)|(aa <=57)):
                pass;
            else:
                aa-=step;
                if(aa<97):
                    bb = 97-aa;
                    aa = 123 - bb;
            print aa;
            bb = chr(aa);
            print bb;
            list_decoderesult.append(bb);
        return list_decoderesult;


def readtext():
    print "****************************home work********************";
    print "function: encode and decode                              ";
    print "1: encode                                                ";
    print "2: decode                                                ";
    print "                                                         ";
    
    filecontent = encodeanddecode();
    f_read = file('message.txt', 'r');
    f = file('plaintext.txt',  'a+');
    ff = file('ciphertext.txt',  'w');
    flag = True;
    i = 0;
    step = 0;
    while(flag):
        user_input = int(raw_input("please input 1 or 2  >>> "));
        if(user_input == 1):
            while(True):
                line =f_read.readline();
                print "111111",line;
                if(len(line) == 0):
                    break;
                if(i == 0):
                    print "xxxxxxxxxxxxxxx";
                    vv = filecontent.encode(line, 0);
                    xx = ord(vv[0]);
                    step = int(chr(xx));
                    print "step is ", step;
                    i+=1;
                    print "vvvvvvvvvvvvv", i;
                else:
                    print "ssssssssssssss", step;
                    vv = filecontent.encode(line, step);
                ss = string.join(vv, '');
                f.write(ss);
        elif(user_input == 2):
            f = file('plaintext.txt',  'a+');
            while(True):
                line =f.readline();
                if(len(line) == 0):
                    break;
                vv = filecontent.decode(line, step);
                ss = string.join(vv, '');
                ff.write(ss);
                flag = False;
        f_read.close();
        f.close();
    ff.close();

readtext();


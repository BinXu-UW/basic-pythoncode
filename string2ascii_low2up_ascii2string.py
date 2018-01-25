#解题思路：他说不能用库里面的大小写转换，所以我们先将字符串转化成ASCII码，然后把ASCII码减去32，然后又转化成字符串，这样就得到结果了
#比如说大写A的ASCII码是65，B是66，小写的a是97，b是98,所以说他们之间的ASCII码相差32，把a转成97然后在减去32，这个32就是大写A的ASCII码。
#这是符合题目要求的，并没有用库提供的大小写转换函数，这是通过ASCII码转化的

def string2ascii_low2up_ascii2string(arg_string):
    for i in range(0, len(arg_string)):
        print chr(ord(arg_string[i])-32),


string = raw_input("please input a string ");
string2ascii_low2up_ascii2string(string);

#问题依然是怎样消除空格,你问下你们老师，到时候你明白了也给我讲讲,我始终不知道这种形式的怎么去掉空格

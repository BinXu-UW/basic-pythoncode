#����˼·����˵�����ÿ�����Ĵ�Сдת�������������Ƚ��ַ���ת����ASCII�룬Ȼ���ASCII���ȥ32��Ȼ����ת�����ַ����������͵õ������
#����˵��дA��ASCII����65��B��66��Сд��a��97��b��98,����˵����֮���ASCII�����32����aת��97Ȼ���ڼ�ȥ32�����32���Ǵ�дA��ASCII�롣
#���Ƿ�����ĿҪ��ģ���û���ÿ��ṩ�Ĵ�Сдת������������ͨ��ASCII��ת����

def string2ascii_low2up_ascii2string(arg_string):
    for i in range(0, len(arg_string)):
        print chr(ord(arg_string[i])-32),


string = raw_input("please input a string ");
string2ascii_low2up_ascii2string(string);

#������Ȼ�����������ո�,������������ʦ����ʱ����������Ҳ���ҽ���,��ʼ�ղ�֪��������ʽ����ôȥ���ո�

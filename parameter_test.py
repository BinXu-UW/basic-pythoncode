# date: 2010/01/29  10AM
# �����Ĵ����Ǻܳ���Ҳ����Ҫ�Ķ�����
#  �ƻ��������׶Σ������ܽắ�����������ã��ڶ����ܽ�ѭ�����ƣ��������ܽ����ݽṹ��


# �����Ĳ�������֮�޲���
def testparameter_null():
    pass;

# �����Ĳ�������֮һ������
def testparameter_one(arg_one):
    print arg_one;

# �����Ĳ�������֮��������
def testparameter_two(arg_one, arg_two):
    print arg_one+arg_two;

# �����Ĳ�������֮������һ��Ԫ����б�ȶ�����������
def testparameter_mutiparameter(list):
    for i in list:
        print i;

# �����Ĳ�������֮Ĭ�ϲ���,�ر�ע�⣬Ĭ�ϲ���ֻ�������һ������
def testdefaultparameter(age, name= "xubin"):
    print name, age;


# �����Ĳ�������֮Ĭ�ϲ���,�ر�ע�⣬��������ָ��λ�õģ�������Ĳ�һ������ϸ����ѧ��Ϊ�ؼ�����
def testkeyparameter(name, age = 20, address ="hubei,yichang"):
    print name,"this year have", age, "old, he's home in", address;

# ����ĳ���һ�������������������б����������Ļ���ô3��������5����10�������Ķ���һ������
# ���ϳ���ȫ�����������ͨ����������ֵһ����������Ƕ����Ϻ����ĵ��ã����򰴺�������Ĵ���





#������ʽ�������Ĳ�������֮�޲���
testparameter_null();

#������ʽ�������Ĳ�������֮һ������
testparameter_one(666);

#������ʽ�������Ĳ�������֮��������
testparameter_two(100, 80);

#������ʽ�������Ĳ�������֮������һ��Ԫ����б�ȶ�����������
list = ["xujie", "xuzhen", "xukun", "xubin"];
testparameter_mutiparameter(list);

#������ʽ�������Ĳ�������֮Ĭ�ϲ���
testdefaultparameter(20);

#������ʽ�������Ĳ���Ϊ�ؼ������������������ֵ�����ʲô����
#ע��ֻ������һ������
testkeyparameter("xubin");
#ע�⴫�ݲ����Ĵ���
testkeyparameter("xukun", address = "hubei.yuanan", age = 25);

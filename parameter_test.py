# date: 2010/01/29  10AM
# 参数的传递是很常用也很重要的东西。
#  计划分三个阶段：今天总结函数参数的运用，第二次总结循环控制，第三次总结数据结构。


# 函数的参数传递之无参数
def testparameter_null():
    pass;

# 函数的参数传递之一个参数
def testparameter_one(arg_one):
    print arg_one;

# 函数的参数传递之两个参数
def testparameter_two(arg_one, arg_two):
    print arg_one+arg_two;

# 函数的参数传递之参数是一个元组或列表既多个参数的情况
def testparameter_mutiparameter(list):
    for i in list:
        print i;

# 函数的参数传递之默认参数,特别注意，默认参数只能是最后一个参数
def testdefaultparameter(age, name= "xubin"):
    print name, age;


# 函数的参数传递之默认参数,特别注意，这种是有指定位置的，和上面的不一样，仔细看，学名为关键参数
def testkeyparameter(name, age = 20, address ="hubei,yichang"):
    print name,"this year have", age, "old, he's home in", address;

# 上面的程序，一个参数，两个参数，列表的如果都理解的话那么3个参数，5个，10个参数的都是一个道理。
# 以上程序全部都编译调试通过，和期望值一样。下面的是对以上函数的调用（次序按函数定义的次序）





#调用形式：函数的参数传递之无参数
testparameter_null();

#调用形式：函数的参数传递之一个参数
testparameter_one(666);

#调用形式：函数的参数传递之两个参数
testparameter_two(100, 80);

#调用形式：函数的参数传递之参数是一个元组或列表既多个参数的情况
list = ["xujie", "xuzhen", "xukun", "xubin"];
testparameter_mutiparameter(list);

#调用形式：函数的参数传递之默认参数
testdefaultparameter(20);

#调用形式：函数的参数为关键参数，看看下面两种调用有什么区别
#注意只传递了一个参数
testkeyparameter("xubin");
#注意传递参数的次序，
testkeyparameter("xukun", address = "hubei.yuanan", age = 25);

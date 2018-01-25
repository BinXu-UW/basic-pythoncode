
# 我自己猜的SUM的内部实现，我估计就是我这样的，可能效率要比我的高，但原理一样


def summ(temp):
    result = 0;
    lenth = len(temp);
    for i in range(1, lenth+1):
        result += list[i-1];
    return result;


#你随便在这个列表里面加入任意整数，你运行下看结果。
list =[1,3,6,9];
print summ(list);




#sum的内部实现也因该和这差不多，无非他是没有把这个内部实现源码公开而已，其实自己也可以写一个DLL。把这段代码放到DLL里面，然后外部调用就直接用就可以了。

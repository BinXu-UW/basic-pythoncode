import sys
import math

#关键逻辑（判断是否为质数）
def isPrime(num):
    if not isinstance(num, int):  #isinstance是系统函数，目的是判断用户输入的NUM是不是一个int,但在前面加了NOT，意义就是取反（
        #简单就是说如果用户输入的不是INT型的数就直接返回，不做任何处理，等于就是说只处理整型）
       return False
    anum = num  #用一个临时变量来存储用户输入的整数
    if anum < 0:   #如果用户输入的小于0
       anum = math.fabs(anum)   #小于0就取绝对值
    if anum == 1:     
       return False
    if anum == 2 or anum == 3:
       return True
    if math.fmod(anum, 2) == 0: #取模运算
       return False
    endN = math.sqrt(anum) + 1  #开方
    i = 3 
    ret = True
    while i < endN: 
       if math.fmod(anum, i) == 0:
          ret = False
          break;
       i += 2
    return ret


def user_input():
    return int(raw_input("please input a int number >>>"))

def main():
    input = user_input()   #函数调用，返回的是用户的输入
    list_result = []  #定义一个空列表
    for i in range(3, input+1):   #循环，从三到输入的数在加1
        try:         #捕获异常
            if(isPrime(i)):    #条件为真则执行下一步（为质数就是真）
                list_result.append(i)   #如果是质数则将其添加到全局的列表中
            else :
                pass
        except ValueError:   #处理异常
            pass       #不做任何处理，这只是告诉你一种捕获异常的方式，以后有实际情况在给你演示，你先混个眼熟，这个很有用
    return list_result   #返回整个列表

print main()

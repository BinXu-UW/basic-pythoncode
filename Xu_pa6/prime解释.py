import sys
import math

#�ؼ��߼����ж��Ƿ�Ϊ������
def isPrime(num):
    if not isinstance(num, int):  #isinstance��ϵͳ������Ŀ�����ж��û������NUM�ǲ���һ��int,����ǰ�����NOT���������ȡ����
        #�򵥾���˵����û�����Ĳ���INT�͵�����ֱ�ӷ��أ������κδ������ھ���˵ֻ�������ͣ�
       return False
    anum = num  #��һ����ʱ�������洢�û����������
    if anum < 0:   #����û������С��0
       anum = math.fabs(anum)   #С��0��ȡ����ֵ
    if anum == 1:     
       return False
    if anum == 2 or anum == 3:
       return True
    if math.fmod(anum, 2) == 0: #ȡģ����
       return False
    endN = math.sqrt(anum) + 1  #����
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
    input = user_input()   #�������ã����ص����û�������
    list_result = []  #����һ�����б�
    for i in range(3, input+1):   #ѭ������������������ڼ�1
        try:         #�����쳣
            if(isPrime(i)):    #����Ϊ����ִ����һ����Ϊ���������棩
                list_result.append(i)   #���������������ӵ�ȫ�ֵ��б���
            else :
                pass
        except ValueError:   #�����쳣
            pass       #�����κδ�����ֻ�Ǹ�����һ�ֲ����쳣�ķ�ʽ���Ժ���ʵ������ڸ�����ʾ�����Ȼ�����죬���������
    return list_result   #���������б�

print main()

def Max(num1,num2,num3):
    num1=input("num1:")
    num2=input("num2:")
    num3=input("num3:")
    max_num=num1
    if max_num < num2:
        max_num=num2
    if max_num < num3:
        max_num=num3

return max_num

def Max2 (list_num):
    list_num=[2,4,-2,10,3]
    max_num=list_num[0]
    for i in range(1,len(list_num)):
        if max_num < list_num[i]:
            max_num=list_num[i]
    return max_num

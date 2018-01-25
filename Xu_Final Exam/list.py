import random
def prim():
    for n in range(2, 1000):
        for x in range(2, n):
            if n % x == 0:
                break;
        else:
            return True


def get_list():
    n=int(raw_input("Enter the range of the list:"))
    nums=[]
    for i in range(n):
      a=random.randint(1,1000)
      nums.append(a)
    return nums

aa = get_list()
for i in aa:
    if(i == 1):
        print i, "is 1";
    elif((i%7==0 )or(i%11==0)or(i%13==0)):
        print i, "is the multiple of 7 or 11 or 13 "
    elif(prim() == True):
        print i ,"is prime"

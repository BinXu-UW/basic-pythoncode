def acceup_input():
    user_input = int(raw_input("������һ����,����0�������>>>>>>"))
    return user_input;

list_result =[];
def invok_self(number):
    list_result.append(number);
    if(number%2==0):
        if(number/2 >1):
            invok_self(number/2)
        elif(number/2 ==1):
            list_result.append(number-1);
            return;
    else:
        invok_self((number*3)+1);


while(True):
    list_result = [];
    user_input = acceup_input();
    if(user_input == 0):
        break;
    invok_self(user_input);
    print list_result

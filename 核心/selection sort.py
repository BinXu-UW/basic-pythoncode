def selection_sort(list_data,size):
    for i in range (size-1):
        max_value=list_data[0]
        index=0
        for j in range (size-1-i):
            if (max_value<list_data[j]):
                max_value=list_data[j]
                index=j
        tep=list_data[size-1-i]
        list_data[size-1-i]=max_value
        list_data[index]=tep

           
def main():
    list_data=[100,5,15,-10,-3]
    list_size=len(list_data)
    print (list_data)
    print list_size
    selection_sort(list_data,list_size)
    print list_data
    print list_size

main()

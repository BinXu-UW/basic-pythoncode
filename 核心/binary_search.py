def binary_search (list1, target):
    found = 0
    left = 0
    right = len(list1) - 1
    
    while found == 0 and left <= right:
        mid = int((left + right) / 2)
        if target == list1[mid] or target == list1[left] or target == list1[right]:
            found = 1
        elif target < list1 [mid]:
            right = mid - 1
        elif target > list1[mid]:
            left = mid + 1
    if found == 1:
        print "Target found at location", mid, left, right
    else:
        print "Sorry, target value could not be found"

def main ():

    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    target = input("Enter an integer target value: ")

    binary_search (list1, target)

main ()

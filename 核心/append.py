list_test = [];
list_test.append(1);
list_test.append(2);
list_test.append(5);


print list_test;
list_test = [];
for i in range(10):
    list_test.append(i);

print list_test;

list_test.remove(2);
print list_test;

zero=[0]*10
print zero
tt=raw_input("Enter a number>>")
print tt
print type(tt)

aa = eval(tt)
print aa
print type(aa)
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.iteritems():
    print k, v

print "11111111111111111111"
knights = {'xk': 'detail xukun', 'xb': 'detail xubin'}
for k, v in knights.iteritems():
    print k, v
print
print
print
print "222222222222"
for kk, vv in knights.iteritems():
    if(kk == 'xb'):
        print kk, vv

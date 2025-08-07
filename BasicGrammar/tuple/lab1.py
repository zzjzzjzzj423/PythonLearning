t1=(1,"hello")
t2=((2,"world"),("hello","Zijian"),123)
print(t1)
print(t2)
print("type:",type(t1),",",t1)

print("type:",type(t2),",",t2)

print(t2[1][0])


tuple_test=(1,"hello",2,33,2,3,2,1)

print(tuple_test.index("hello"))
print(tuple_test.count(1))
print(len(tuple_test))


count=0
print("-------------------")
while count<len(tuple_test):
    print(tuple_test[count])
    count=count+1
print("-------------------")
for i in range(0,len(tuple_test)):
    print(tuple_test[i])
list_test=[21,25,21,23,22,20]

list_test.append(31)

append_list=[29,33,30]

list_test.extend(append_list)
print(list_test.pop(0))
print(list_test[len(list_test)-1])

print(list_test.index(31))

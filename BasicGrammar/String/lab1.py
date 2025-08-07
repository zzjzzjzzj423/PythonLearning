my_str="azkckaas-_sadad"

print(my_str[1])
print(my_str[-1])
print(my_str.index("-_"))

new_str=my_str.replace("as","oooo")

print(new_str)


str_list="1,2,3,4,5,6,7,8,9,10"

new_list=str_list.split(",")
print(new_list)

test_list="aos1234aos"
after_test_list=test_list.strip("aos")
print(after_test_list)

print(test_list.count("aos"))

print(len(test_list))

my_dict={"王力宏":99,"周杰伦":88,"林俊绝":77}
my_dict1={}
my_dict2=dict()


print(my_dict["周杰伦"])


stu_grade_dict={
    "王力宏":{"语文":99,"数学":100,"英语":100},
    "周杰伦":{"语文":92,"数学":10,"英语":1000},
    "林俊绝":{"语文":9,"数学":1,"英语":1}
}

print(stu_grade_dict)

print(stu_grade_dict["林俊绝"]["语文"])

my_dict["周子健"]=100
my_dict["王力宏"]=22
print(my_dict)

my_dict.pop("周子健")
print(my_dict)

keys_list=my_dict.keys()

print(keys_list)

for key in keys_list:
    print(my_dict[key])




my_list=[1,2,3,4,5,"student"]

index=my_list.index(2)

append_list=["sa","hcw"]

my_list.insert(2,"zzj")

print(my_list[-1])
print(index)
print(my_list)

my_list.extend(append_list)
print(my_list)

print("------------------------------------")
del my_list[2]
print(my_list)

my_list.insert(2,"zzj")
print(my_list)

my_list.pop(2)
print(my_list)

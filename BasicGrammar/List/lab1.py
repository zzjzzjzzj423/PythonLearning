name_list=["qw",1,2,3,"1sad"]

for i in name_list:
    print(i)


list_e=[]

for i in range(1,20):
    list_e.append(i)

print("type:",type(list_e),", list_e:",list_e)

list_f=list()
for i in range(1,11):
    list_f.append(i)

print("type:",type(list_f),",list_f:",list_f)

embed_list=[[1,2,3],[4,5,6],[7,8,9]]
print("type:",type(embed_list),", embed_list:",embed_list)

print("----------------------------------")

for i in embed_list:
    for j in i:
        print(j)

print("----------------------------------")

for i in range(list_f.__len__()):
    print(list_f[i])


print("----------------------------------")
print(list_e[-1])

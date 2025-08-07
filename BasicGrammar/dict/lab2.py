dict_lab={"lihong wang":{"department":"IT"  ,"salary":3000,"level":1},
            "Jay Zhou":{"department":"Market" ,"salary":5000,"level":2},
          "JJ":{"department":"Market" ,"salary":7000,"level":3},
          "xueyou zhang":{"department":"IT" ,"salary":4000,"level":1},
          "dehua Liu":{"department":"Market" ,"salary":6000,"level":2},
}

for key in dict_lab:
    if dict_lab[key]["level"]==1:
        dict_lab[key]["salary"]=dict_lab[key]["salary"]+1000


for key in dict_lab:
    print(dict_lab[key])


name="传智播客"
gjdm="003032"
price=19.99

k=1.2
days=7
afterPrice=71.63

print("Please tell me your name:")
real_name=input()
print("welcome!",real_name)
message1=f"公司:{name}, 股票代码:{gjdm}， 当前股价:{price}"
print(message1)
messgae2="每日增长系数是：%.1f, 经过%d天增长后, 股价达到了%.2f" %(k,days,afterPrice)

age=19

print(messgae2)

if age>=18:
    print("我陈年")

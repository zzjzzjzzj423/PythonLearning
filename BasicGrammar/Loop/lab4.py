num=int(input())
for i in range(1,num+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz,",i)
    elif i%5==0:
        print("Buzz,i",i)
    elif i%3==0:
        print("Fizz,i",i)
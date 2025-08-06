import random

num=random.randint(1,10)
guess=int(input("输入:"))
if guess==num:
    print("correct")
else:
    if guess>num:
        print("incorrect and more")
    else:
        print("incorrect and less")

    guess=int(input("remain twice:"))

    if guess==num:
        print("correct")
    else:
        if guess>num:
            print("incorrect and more")
        else:
            print("incorrect and less")
        guess=int(input("remain once:"))
        if guess==num:
            print("correct")
        else:
            if guess>num:
                print("incorrect and more")
            else:
                print("incorrect and less")
        print(f"you don't have chance, the answer was {num}")
def is_even(num):
    return num % 2 == 0


num=int(input("Enter a number: "))
if is_even(num):
    print("Even")
else:
    print("Odd")
num=str(123)
print(type(num),num)


float_num=float("1232.213")

print(type(float_num),float_num)

print("result:",int(num)+float("1232.213"))


print("2 square:",2**3)

meme="asd"

print("ascade:%s" % meme)


message="kind--,%s-,%.3f" % (meme, float_num)
print(message)

name="zzzz"
age=12

test=f"name:{name}, age:{age}"
print(test)
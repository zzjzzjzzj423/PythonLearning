import time

f=open("/Users/zijian/Public/code_p/PythonLearning/BasicGrammar/File/test/text1","r",encoding="utf-8")

for line in f:
    print(line)

f.close()

f=open("/Users/zijian/Public/code_p/PythonLearning/BasicGrammar/File/test/text2","w",encoding="utf-8")

f.write("hello")

f.close()

f=open("/Users/zijian/Public/code_p/PythonLearning/BasicGrammar/File/test/text2","a",encoding="utf-8")

f.write("world")
f.close()



# def ninenine():
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print(f"{j}*{i}={i*j}",end=' ')
#         print("\n")

# ninenine()

# def hanoi(n,a,b,c):
#     if n == 1:
#         print(f"{a} -> {c}")
#     else:
#         hanoi(n-1,a,c,b)
#         print(f"{a} -> {c}")
#         hanoi(n-1,b,a,c)

# hanoi(4,'A','B','C')


#例题 1：字符串操作
# 编写一个 Python 函数，该函数接受一个字符串作为输入，并返回一个新字符串，其中原字符串的所有单词的首字母大写。

def capi(word):
    word2 = word.title()
    print(word2)


capi("hello world")

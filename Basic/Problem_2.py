# #local Variable


# def add():
#     a=20
#     b=30
#     c=a+b
#     print("the sum is:",c)
# add()


# #global Variable

x=101
def mainfunction():
    global x
    print(x)
    x="welcome to java"
    print(x)
mainfunction
print(x)    
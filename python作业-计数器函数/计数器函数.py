def counter(func):
    def inner():
        global num  #修改全局变量需要使用 global
        func()
        num += 1
    return inner

@counter
def show():
    pass

if __name__ == '__main__':
    num = 0
    for i in range(0, 5):
        show()
    print("show函数调用的次数：",num)


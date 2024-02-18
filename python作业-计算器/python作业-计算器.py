#定义计算函数
def calculator(a,b,char):
    if char == '+':
        sum = a + b
    elif char == '-':
        sum = a - b
    elif char == '*':
        sum = a * b
    elif char == '/':
        sum = a / b
    print("运算结果为：",sum)

if __name__ == "__main__":

    print('请输入两个数字和运算符(+、-、*、/):')
    try:
        a = float(input())
    except ValueError:
        print("输入的不是数字,请重新输入：")
        a = float(input())

    try:
        b = float(input())
    except ValueError:
        print("输入的不是数字,请重新输入：")
        b = float(input())

    char = str(input())

    try:
        calculator(a,b,char)
    except ZeroDivisionError:
        print("除数不能为0")
    except Exception:
        print("程序运行出错，请检查代码")

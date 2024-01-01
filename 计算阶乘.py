def fac():
    num = int(input("input: "))
    factorial = 1

    if num < 0:
        print("负数没有阶乘")
    elif num == 0:
        print("1")
    else:
        for i in range(1,num + 1):
            factorial *= i
        print("%d阶乘: %d" % (num, factorial))

def factorial(n):
    res = n
    for i in range(1, n):
        res *= i
    return  res

def fact(n):
    if n == 1:
        return 1
    return n*fact(n - 1)


print(fact(3))
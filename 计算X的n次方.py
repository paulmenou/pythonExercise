def power(x,n):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s

print(pow(2,3))
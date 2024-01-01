def lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            l = greater
            break
        greater += 1
    return l

print(lcm(14,16))

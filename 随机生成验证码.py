import  random,string
list1 =[]
for i in range(65,91):
    list1.append(chr(i))
for i in range(97,123):
    list1.append(chr(i))
for i in range(48, 58):
    list1.append(chr(i))
ma = random.sample(list1,6)
print(ma)
ma = ''.join(ma)
print(ma)


str1 = "0123456789"
str2 = string.ascii_letters #
str3 = str1 + str2
print(str3)
ma1 = random.sample(str3,6)
ma1 = ''.join(ma1)
print(ma1)

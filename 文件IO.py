with open("test.txt","wt") as out_file:
    out_file.write("xiewenjiana ")

with open("test.txt","rt") as in_file:
    text = in_file.read()

print(text)
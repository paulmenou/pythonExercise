import os
def print_dir():
    filepath = input("lujing:")
    if filepath == "":
        print("once again")
    else:
        for i in os.listdir(filepath):
            path = (os.path.join(filepath, i))
            print(path)

print_dir()





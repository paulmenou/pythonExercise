import os
def show_dir(filepath):
    for i in os.listdir(filepath):
        path = (os.path.join(filepath, i))
        print(path)
        if(os.path.isdir(path)):
            show_dir(path)


filepath = '/home/jason/Desktop'

show_dir(filepath)
import os

def getParentDir(path):
    return os.path.dirname(path)


# file open feature
def openFile(path):
    file = open(path, 'r')
    str = file.read()
    return print(str)
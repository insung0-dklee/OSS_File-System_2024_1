import os

def getParentDir(path):
    return os.path.dirname(path)

#Add function to create directory through path
def makeDir(path):
    return os.mkdir(path)
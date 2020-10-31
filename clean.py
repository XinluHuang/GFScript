import os
import os.path as path
import shutil


def clean(root, depth, *deleteFileNames):
    list = os.listdir(root)
    for file in list:
        realFile = path.join(root, file)
        if deleteFileNames.__contains__(file):
            print("delete " + realFile)
            if path.isdir(realFile):
                shutil.rmtree(realFile)
            else:
                os.remove(realFile)
        elif path.isdir(realFile) and depth > 0:
            clean(realFile, depth - 1, *deleteFileNames)


root = path.dirname(path.abspath(__file__))
clean(root, 1, "log", "log.txt", "log.html", "trace.txt")

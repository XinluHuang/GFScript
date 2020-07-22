from airtest.core.api import *
import os

# exists(Template(r"tpl1595666514523.png", record_pos=(-0.317, -0.312), resolution=(1080, 2340)))
CommomImageRoot = os.path.join(os.path.dirname(__file__), "image")
LocalImageRoot = [CommomImageRoot]

cache = {}
SUFFIX = ".png"


def getImageTemplate(prefix):
    if type(prefix) != str:
        raise Exception("不是字符串,类型错误")
    file_name = prefix + SUFFIX
    if cache.get(file_name):
        return cache.get(file_name)
    else:
        for local in LocalImageRoot:
            file_path = os.path.join(local, file_name)
            if os.path.exists(file_path):
                res = Template(file_path)
                cache[file_name] = res
                return res
        return False


def addLocalImageRoot(root):
    if type(root) != str:
        raise Exception("类型错误")
    LocalImageRoot.insert(0, root)

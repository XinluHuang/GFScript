from airtest.core.api import *
import os
from airtest.utils.transform import TargetPos

CommomImageRoot = os.path.join(os.path.dirname(__file__), "image")
LocalImageRoot = [CommomImageRoot]

cache = {}
SUFFIX = ".png"


def getImageTemplate(file_name, threshold=None, target_pos=TargetPos.MID, record_pos=None, resolution=(), rgb=False):
    if type(file_name) != str:
        raise Exception("不是字符串,类型错误")
    file_name = str.split(file_name, '.')[0] + SUFFIX
    if cache.get(file_name):
        return cache.get(file_name)
    else:
        for local in LocalImageRoot:
            file_path = os.path.join(local, file_name)
            if os.path.exists(file_path):
                res = Template(file_path, threshold, target_pos, record_pos, resolution, rgb)
                cache[file_name] = res
                return res
        return False


def addLocalImageRoot(root):
    if type(root) != str:
        raise Exception("类型错误")
    LocalImageRoot.insert(0, root)

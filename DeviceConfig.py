import Const
import os


class DeviceConfig:
    CMD = None
    DEV = None
    SERIAL = None
    # 一级战斗页面
    BLANK = None
    SCHEDULE = None
    END_BEGIN = None
    TERMINATE = None
    FAIRY_ON_OFF_ONCE = None
    FAIRY_ON_OFF_PERSISTENT = None
    # 二级梯队页面
    ECHELON_SUPPLY = None
    ECHELON_WITHDRAW = None
    ECHELON_CANCEL = None
    ECHELON_REPAIRE_FAST = None
    # 添加梯队
    ECHELON_ADD_CERTAIN = None
    ECHELON_ADD_CANCEL = None
    # 对话框
    DIALOG_CERTAIN = None
    DIALOG_CANCEL = None
    # 终止作战对话框
    TERMINATE_RENEW = None


def getDeviceConfig(t=None):
    if type(t) != int:
        devices = []
        res = os.popen("adb devices").readlines()
        for inx, line in enumerate(res):
            if inx == 0 or str.strip(line) == "" or str.__contains__(line, "devices") or str.__contains__(line, "List"):
                continue
            devices.append(str.split(line, '\t')[0])
        devicesCount = len(devices)
        if devicesCount <= 0:
            raise Exception("找不到设备")
        elif devicesCount >= 2:
            raise Exception(str.format("找到%d台设备,不能确认" % devicesCount))
        else:
            return creatSerialConfig(devices[0])
    if t == Const.CONNECT_TYPE_PHONE:
        return creatPhoneConfig()
    elif t == Const.CONNECT_TYPE_WIFI:
        instance = creatPhoneConfig()
        instance.DEV = "Android://127.0.0.1:5037/192.168.0.230:5555?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH"
        instance.CMD = "adb -s 192.168.0.230:5555 shell input swipe "
        return instance
    else:
        raise Exception("暂不支持其他类型")


def creatPhoneConfig():
    instance = DeviceConfig()
    instance.CMD = "adb -d shell input swipe "
    instance.SERIAL = "e9cc22c5"
    instance.DEV = "Android://127.0.0.1:5037/" + instance.SERIAL + "?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH"

    initButton(instance)
    return instance


def creatSerialConfig(serial):
    if type(serial) != str:
        raise Exception("类型错误")
    instance = DeviceConfig()
    instance.SERIAL = serial
    instance.CMD = "adb -s " + serial + " shell input swipe "
    instance.DEV = "Android://127.0.0.1:5037/" + serial + "?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH"

    initButton(instance)
    return instance


def initButton(dev):
    if type(dev) != DeviceConfig:
        raise Exception("类型错误")
    dev.BLANK = (1589, 62)
    dev.SCHEDULE = (157, 893)
    dev.END_BEGIN = (2120, 972)
    dev.TERMINATE = (502, 79)
    dev.FAIRY_ON_OFF_ONCE = (2195, 622)
    dev.FAIRY_ON_OFF_PERSISTENT = (2183, 335)

    dev.ECHELON_SUPPLY = (1971, 833)
    dev.ECHELON_WITHDRAW = (1667, 966)
    dev.ECHELON_CANCEL = (1937, 955)

    dev.ECHELON_ADD_CERTAIN = dev.ECHELON_CANCEL

    dev.DIALOG_CERTAIN = (1311, 756)
    dev.DIALOG_CANCEL = (993, 756)

    dev.TERMINATE_RENEW = (944, 732)

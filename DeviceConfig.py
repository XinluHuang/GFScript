import Const


class DeviceConfig:
    CMD = None
    DEV = None
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


def getDeviceConfig(t):
    if type(t) != int:
        raise Exception("输入类型不为数字")
        return False
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
    instance.DEV = "Android://127.0.0.1:5037/e9cc22c5?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH"

    instance.BLANK = (1589, 62)
    instance.SCHEDULE = (157, 893)
    instance.END_BEGIN = (2120, 972)
    instance.TERMINATE = (502, 79)
    instance.FAIRY_ON_OFF_ONCE = (2195, 622)
    instance.FAIRY_ON_OFF_PERSISTENT = (2183, 335)

    instance.ECHELON_SUPPLY = (1971, 833)
    instance.ECHELON_WITHDRAW = (1667, 966)
    instance.ECHELON_CANCEL = (1937, 955)

    instance.ECHELON_ADD_CERTAIN = instance.ECHELON_CANCEL

    instance.DIALOG_CERTAIN = (1311, 756)
    instance.DIALOG_CANCEL = (993, 756)

    instance.TERMINATE_RENEW = (944, 732)
    return instance

import random, platform

def getPositionWithRange(v, ran):
    if type(v) == tuple and v.__len__() == 2:
        return (
            v[0] + random.randint(-ran, ran),
            v[1] + random.randint(-ran, ran)
        )
    else:
        raise Exception("类型不正确")


def getTouchCMD(cmd, v, duration):
    return getSwipeCMD(cmd, v, v, duration)


def getSwipeCMD(cmd, source, destination, duration):
    return str.format(
        "%s %d %d %d %d %d %d" % (cmd, source[0], source[1], destination[0], destination[1], duration[0], duration[1]))


def getSwitchPos(pos):
    return pos[0] - 100, pos[1]


def getAssistWaitPos(pos):
    return pos[0], pos[1] + 130


def checkTupleLength2(obj):
    return type(obj) == tuple and obj.__len__() == 2


def getPlatform():
    platform.system().__str__()



import abc
import os
import random

from airtest.cli.parser import cli_setup
from airtest.core.api import Template, time, auto_setup, exists

import Const
import DeviceConfig
import ImageUtil
import Util


class Application:
    config = None

    CLICK_RANGE = 13
    SWIPE_RANGE = 50
    TOUCH_DURATION = (100, 200)
    SWIPE_DURATION = (500, 800)

    @abc.abstractmethod
    def filePath(self):
        pass

    def __init__(self):
        self.config = DeviceConfig.getDeviceConfig(Const.CONNECT_TYPE_PHONE)
        if not cli_setup():
            auto_setup(self.filePath(), logdir=True, devices=[
                self.config.DEV,
            ])
        ImageUtil.addLocalImageRoot(os.path.dirname(self.filePath()))

    @staticmethod
    def sleep(t):
        time.sleep(t + random.uniform(0, 0.3))

    def touch(self, obj, sleep_time=1):
        if type(obj) == Template:
            obj = self.exists(obj)
        elif type(obj) == tuple and obj.__len__() == 2:
            pass
        else:
            raise Exception("类型不是长度为2的元组")
        pos = Util.getPositionWithRange(obj, self.CLICK_RANGE)
        os.system(Util.getTouchCMD(self.config.CMD, pos, self.TOUCH_DURATION))
        self.sleep(sleep_time)

    def swipe(self, source, destination, sleep_time=1):
        source = Util.getPositionWithRange(source, self.SWIPE_RANGE)
        destination = Util.getPositionWithRange(destination, self.SWIPE_RANGE)
        os.system(Util.getSwipeCMD(self.config.CMD, source, destination, self.SWIPE_DURATION))
        self.sleep(sleep_time)

    @staticmethod
    def exists(obj):
        return exists(obj)

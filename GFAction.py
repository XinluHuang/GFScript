import abc
import traceback
import os

from airtest.core.api import Template, loop_find, TargetNotFoundError, time
from airtest.report.report import simple_report

import Application
import Util


class GFAction(Application.Application):
    map = {}
    refList = []  # (Template,expectedXY)
    COMPENSATE_TIME = 3
    run_times = None
    now_times = None
    TRACE_PATH = os.path.abspath("trace.txt")

    @abc.abstractmethod
    def filePath(self):
        pass

    def __init__(self):
        super().__init__()
        # log_path = os.path.join(os.path.dirname(os.path.abspath(self.filePath())), "log")
        # if os.path.exists(log_path):
        #     shutil.rmtree(os.path.join(os.path.dirname(os.path.abspath(self.filePath())), "log"))

    def addCompensateTuple(self, template, expectedXY):
        self.refList.append((template, expectedXY))

    @abc.abstractmethod
    def compensateConfig(self):
        pass

    def compensate(self):
        self.refList.clear()
        self.compensateConfig()
        i = 0
        while i < self.COMPENSATE_TIME:
            for entry in self.refList:
                template = entry[0]
                expectedXY = entry[1]
                nowXY = self.existsFast(template)
                if nowXY:
                    delta = (nowXY[0] - expectedXY[0], nowXY[1] - expectedXY[1])
                    for key in self.map.keys():
                        old = self.map[key]
                        self.map[key] = (old[0] + delta[0], old[1] + delta[1])
                    return
                else:
                    continue
            i = i + 1
        raise BaseException(str.format("找不到参照点,重复%d次" % self.COMPENSATE_TIME))

    def getMap(self):
        return self.map

    def touchBlank(self, sleep_time=1):
        self.touch(self.config.BLANK)
        self.sleep(sleep_time)

    def touch(self, obj, sleep_time=1):
        if type(obj) == Template:
            pass
        elif type(obj) == tuple and obj.__len__() == 2:
            pass
        elif type(obj) == str:
            obj = self.map[obj]
        else:
            raise Exception("类型不正确" + obj.__str__())
        return super().touch(obj, sleep_time)

    def supply(self, key):
        self.touch(key)
        self.touch(key)
        self.touch(self.config.ECHELON_SUPPLY)
        self.touchBlank()
        self.sleep(1)

    def switch(self, key1, key2):
        self.touch(key1)
        self.touch(key2)
        self.touch(Util.getSwitchPos(self.map[key2]))
        self.touchBlank()

    def addEchelon(self, v, sleep_time=1):
        self.touch(v)
        self.touch(self.config.ECHELON_ADD_CERTAIN)
        self.sleep(sleep_time)

    def beginOrEnd(self):
        self.touch(self.config.END_BEGIN)

    def begin(self):
        self.beginOrEnd()
        self.sleep(3)

    def endTurn(self):
        self.beginOrEnd()

    def withdrawEchelon(self, key, sleep_time=1):
        self.touch(key)
        self.touch(key)
        self.touch(self.config.ECHELON_WITHDRAW)
        self.touch(self.config.DIALOG_CERTAIN)
        self.sleep(1)
        self.sleep(sleep_time)

    def schedule(self, key1, key2):
        self.touch(self.config.SCHEDULE)
        self.touch(key1)
        self.touch(key2)

    def sleepUntilAssert(self, sleep_time, picture, interval=10, time_range=20):
        self.sleep(sleep_time - time_range)
        times = int((2 * time_range) / interval)
        i = 0
        while i < times:
            if not self.existsFast(picture):
                self.sleep(10)
            else:
                self.sleep(3)
                return
            i = i + 1
        raise Exception("找不到图片" + picture.__str__())

    def renew(self, sleep_time=4):
        self.touch(self.config.TERMINATE)
        self.touch(self.config.TERMINATE_RENEW)
        self.sleep(sleep_time)

    @staticmethod
    def existsFast(tem):
        try:
            return loop_find(tem, timeout=1, interval=0.1)
        except TargetNotFoundError:
            return False

    def run(self, times=None):
        if times:
            self.run_times = times
        if not self.run_times:
            self.run_times = int(input("input times\n"))
        self.now_times = 0
        try:
            i = 0
            while i < self.run_times:
                self.step()
                i = i + 1
                self.now_times = i
                print(str.format("第%d次,剩余%d次" % (self.now_times, self.run_times - self.now_times)))
                print(str.format("第%d次,剩余%d次" % (self.now_times, self.run_times - self.now_times)))
                print(str.format("第%d次,剩余%d次" % (self.now_times, self.run_times - self.now_times)))
        except Exception as e:
            f = open(self.TRACE_PATH, 'w', encoding="UTF-8")
            traceback.print_exc(None, f, True)
            localtime = time.asctime(time.localtime(time.time()))
            f.write(localtime.__str__() + "\n")
            f.flush()
            f.close()
            os.system("start " + self.TRACE_PATH)
            # print(traceback.format_exc())
            traceback.print_exc()
        finally:
            simple_report(self.filePath(), logpath=True)

    def getNowTimes(self):
        return self.now_times

    @abc.abstractmethod
    def step(self):
        pass

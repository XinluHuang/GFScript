import sys

from airtest.core.api import *

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import GFAction, logging
from ImageUtil import getImageTemplate as find

hq = "hq"
e1 = "e1"
ap = "ap"
ehq = "ehq"


class Controller(GFAction.GFAction):
    list = None
    first = True

    def filePath(self):
        return __file__

    def compensateConfig(self):
        dic = self.getMap()
        dic[hq] = (896, 542)
        dic[e1] = (1455, 377)
        dic[ehq] = (1455, 212)
        t = find(r"hq.png")
        self.addCompensateTuple(t, (896, 542))

    def test(self):
        print(find_all(Template(r"enter2.png", record_pos=(0.157, 0.06), resolution=(2340, 1080))))
        pass

    def step(self):
        res = self.findAll(find(r"enter2.png"), find(r"enter.png"))
        if not res:
            raise Exception("找不到入口")
        res = res[0]
        res = (res[0] + 20, res[1] + 20)
        logging.info("res is " + res[0].__str__())
        print("res is " + res[0].__str__())
        self.touch(res)
        self.sleep(1)
        self.touch(find("battle_confirm"))
        self.sleep(5)

        self.compensate()
        self.addEchelon(hq)
        self.begin()

        self.supply(hq)
        self.schedule(hq, ehq)
        self.touch(e1)
        self.endTurn()

        self.sleepUntilAssert(91, find("achievement_settlement"))
        self.touchBlank()
        self.touchBlank()
        self.touchBlank()
        self.touchBlank()
        self.touchBlank()
        self.touchBlank()
        self.touchBlank()
        self.sleep(4)


c = Controller()
c.run()
# c.test()

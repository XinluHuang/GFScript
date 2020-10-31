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
        dic[hq] = (1170, 543)
        dic[e1] = (1168, 310)
        dic[ehq] = (1168, 235)
        t = find(r"hq_icon.png")
        self.addCompensateTuple(t, (1170, 543))

    def step(self):
        res = self.findAll(find(r"enter_normal.png"), find(r"enter_small.png"))
        if not res:
            raise Exception("找不到狂欢夜行入口")
        logging.info("res is " + res.__str__())
        temp = res[0]
        for i in range(0, res.__len__()):
            if res[i][0] < temp[0] and res[i][1] > temp[1]:
                temp = res[i]
        self.touch(temp)
        self.touch(find("battle_confirm"))
        self.sleep(5)

        self.compensate()
        self.addEchelon(hq)
        self.begin()
        self.supply(hq)
        self.schedule(hq, ehq)
        self.touch(e1)
        self.touch(ehq)
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

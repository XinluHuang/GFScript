import sys

from airtest.core.api import *

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import GFAction
from ImageUtil import getImageTemplate as find

hq = "hq"
e0 = "e0"
e1 = "e1"
e2 = "e2"
e3 = "e3"
ap = "ap"
ehq = "ehq"
apl = "apl"
apr = "apr"




class Controller(GFAction.GFAction):
    list = None
    first = True

    def filePath(self):
        return __file__

    def compensateConfig(self):
        dic = self.getMap()
        dic[hq] = (982, 554)
        dic[e1] = (1284, 538)
        dic[e2] = (1284, 855)
        self.addCompensateTuple(find("hq"), (982, 554))

    def test(self):
        print(exists(find("hq")))
        # hq (982, 554)
        # e1 1284 538
        # e2 1284 855

        pass

    def step(self):
        big=find("ningshi_big")
        normal=find("ningshi")
        if self.existsFast(big):
            self.touch(big)
        else:
            self.touch(normal)
        self.sleep(2)
        self.touch(find("battle_confirm"))
        self.sleep(9)

        self.compensate()
        self.addEchelon(hq)
        self.begin()

        self.supply(hq)
        self.schedule(hq, e1)
        self.touch(e2)
        self.touch(e1)
        self.endTurn()

        self.sleepUntilAssert(130, find("achievement_settlement"))
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

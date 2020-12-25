import sys

from airtest.core.api import *


sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import GFAction, logging
from ImageUtil import getImageTemplate as find


hq = "hq"
e0="e0"
e1 = "e1"
e2 = "e2"
e3 = "e3"
ap = "ap"
ehq = "ehq"
apl="apl"
apr="apr"



class Controller(GFAction.GFAction):
    list = None
    first = True

    def filePath(self):
        return __file__

    def compensateConfig(self):
        dic = self.getMap()
        dic[hq] = (1156, 546)
        dic[apl] = (790, 130)
        dic[apr] = (1522, 218)
        dic[e0] = (716, 600)
        dic[e1] = (973, 477)
        dic[e2] = (1424, 400)
        dic[e3] = (928, 235)
        v = find("hq")
        self.addCompensateTuple(v, (1166, 556))

    def test(self):
        pass

    def step(self):
        self.touch(find("txy"),2)
        self.touch(find("normal_battle"))
        self.sleep(7)

        self.swipe(self.existsFast(find("hq")),(1289,796),2)
        self.compensate()
        self.touchBlank()
        self.addEchelon(apl)
        self.addEchelon(hq)
        self.addEchelon(apr)
        self.begin()

        self.supply(apl)
        self.supply(hq)
        self.supply(apr)
        self.schedule(apl, e0)
        self.touch(e1)
        self.touchBlank()
        self.touch(hq)
        self.touch(e2)
        self.touchBlank()
        self.touch(apr)
        self.touch(e3)
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

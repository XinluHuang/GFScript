import sys

from airtest.core.api import *

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import GFAction
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
        dic[hq] = (1069, 470)
        dic[e1] = (1403, 817)
        dic[ap] = (717, 632)
        dic[ehq] = (1309, 985)
        t = find(r"hq_icon.png")
        self.addCompensateTuple(t, (1069, 470))

    def step(self):
        enter = find(r"kdjx.png")
        assert_exists(enter, "开袋惊喜")
        self.touch(enter)
        self.touch(find("normal_battle"))
        self.sleep(5)

        self.compensate()
        self.addEchelon(hq)
        self.addEchelon(ap)
        self.begin()
        self.supply(hq)
        self.schedule(hq, ehq)
        self.touch(e1)
        self.endTurn()

        self.sleepUntilAssert(61, find("achievement_settlement"))
        self.touchBlank()
        self.touchBlank()
        self.touchBlank()
        self.touchBlank()
        self.touchBlank()
        self.touchBlank()
        self.sleep(4)


c = Controller()
c.run()

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
        dic[hq] = (1100, 539)
        dic[e1] = (1587, 537)
        dic[e2] = (1420, 537)
        self.addCompensateTuple(find("hq"), (1100, 539))

    def test(self):
        print(exists(find("hq")))
        # 1100 539

        # e1 1587 537
        # e2 1420 537

        pass

    def step(self):
        anliu = find("anliu")
        if self.existsFast(anliu):
            self.touch(anliu)
        self.touch(find("normal_battle"))
        self.sleep(6)

        self.compensate()
        self.addEchelon(hq)
        self.begin()
        self.sleepUntilAssert(22, find("mission_brief"))
        self.touch(self.config.DIALOG_BACK)

        self.supply(hq)
        self.schedule(hq, e1)
        self.touch(e2)
        self.endTurn()

        self.sleepUntilAssert(110, find("achievement_settlement"))
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

import sys

from airtest.core.api import *

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import GFAction
import ImageUtil
import random

hq = "hq"
e1 = "e1"


class Controller(GFAction.GFAction):
    list = None
    first = True

    def filePath(self):
        return __file__

    def compensateConfig(self):
        dic = self.getMap()
        dic[hq] = (820, 536)
        dic[e1] = (1473, 541)
        t = ImageUtil.getImageTemplate(r"tip.png")
        self.addCompensateTuple(t, (976, 477))

    def step(self):
        row = random.randint(0, 500) + 320
        self.swipe((1910, row), (428, row))
        self.swipe((1910, row), (428, row))
        self.sleep(1)

        v1 = self.existsFast(ImageUtil.getImageTemplate(r"enter.png"))
        v1 = (v1[0] + 80, v1[1])
        self.touch(v1)
        self.touch(ImageUtil.getImageTemplate("battle_confirm"))
        assert_exists(ImageUtil.getImageTemplate("battle_begin"), "开始作战")

        self.compensate()
        self.addEchelon(hq)
        self.begin()
        if self.now_times == 0:
            self.touch(hq)
            if self.existsFast(ImageUtil.getImageTemplate("fairy_off")):
                self.touch(ImageUtil.getImageTemplate("fairy_off"))
            self.touchBlank()
        self.supply(hq)
        self.schedule(hq, e1)
        self.endTurn()

        self.sleepUntilAssert(121, ImageUtil.getImageTemplate("achievement_settlement"))
        self.touchBlank()
        self.touchBlank()
        self.touchBlank()
        self.touchBlank()
        self.touchBlank()
        self.sleep(4)


c = Controller()
c.run()

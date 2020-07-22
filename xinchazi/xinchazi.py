import sys

from airtest.core.api import *

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import GFAction
import ImageUtil
import Util

hq = "hq"
e1 = "e1"
e2 = "e2"
e3 = "e3"


class Controller(GFAction.GFAction):

    def filePath(self):
        return __file__

    def compensateConfig(self):
        dic = self.getMap()
        dic[hq] = (1145, 539)
        dic[e1] = (1017, 574)
        dic[e2] = (995, 457)
        dic[e3] = (1326, 768)
        self.addCompensateTuple(ImageUtil.getImageTemplate("anjielika"), (1061, 419))

    def step(self):
        v1 = self.existsFast(ImageUtil.getImageTemplate("chazi"))
        v2 = self.existsFast(ImageUtil.getImageTemplate("chazi2"))
        if v1:
            self.touch(v1)
        elif v2:
            self.touch(v2)
        else:
            raise Exception("找不到新叉子")

        self.touch(ImageUtil.getImageTemplate("battle_confirm"))
        self.sleep(5)

        assert_exists(ImageUtil.getImageTemplate("battle_begin"), "开始作战")
        self.compensate()
        self.addEchelon(hq)
        self.begin()

        self.supply(hq)
        self.touchBlank()
        self.touch(e2)
        self.touch(e2)
        self.touch(Util.getAssistWaitPos(self.map.get(e2)))
        self.touchBlank()
        self.schedule(hq, e1)
        self.touch(hq)
        self.touch(e1)
        self.touch(hq)
        self.touch(e1)
        self.endTurn()
        self.sleepUntilAssert(81, ImageUtil.getImageTemplate("one"))
        self.compensate()
        self.touchBlank()
        self.addEchelon(hq)
        self.supply(hq)
        self.schedule(hq, e3)

        self.endTurn()

        self.sleepUntilAssert(71, ImageUtil.getImageTemplate("return_base"))
        self.touchBlank()
        self.touchBlank()
        self.touchBlank()
        self.touchBlank()
        self.touchBlank()
        self.touchBlank()
        self.sleep(8)


c = Controller()
c.run()

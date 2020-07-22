import sys

from airtest.core.api import *

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import GFAction
import ImageUtil

hq = "hq"
apl = "apl"
e1 = "e1"


class Controller(GFAction.GFAction):
    list = None
    first = True

    def filePath(self):
        return __file__

    def compensateConfig(self):
        dic = self.getMap()
        dic[hq] = (1321, 801)
        dic[apl] = (679, 400)
        dic[e1] = (821, 631)
        t = ImageUtil.getImageTemplate("fangyumen")
        self.addCompensateTuple(t, (1509, 741))

    def step(self):
        assert_exists(ImageUtil.getImageTemplate("battle_begin"), "开始作战")
        if self.first:
            self.up()
            self.first = False
        self.compensate()
        self.addEchelon(apl)
        self.addEchelon(hq)
        self.begin()

        self.supply(apl)
        self.schedule(apl, e1)
        self.touch(apl)
        self.endTurn()
        self.sleepUntilAssert(61, ImageUtil.getImageTemplate("fairy_instruction"))

        self.compensate()
        self.touchBlank()
        self.withdrawEchelon(apl)
        self.renew()
        self.sleep(5)

    def up(self):
        self.swipe(
            self.existsFast(ImageUtil.getImageTemplate("fangyumen"))
            , (1509, 741))


c = Controller()
c.run()

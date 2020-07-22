import sys

from airtest.core.api import *

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import GFAction
import ImageUtil

hq = "hq"
apl = "apl"
apr = "apr"
hqe = "hqe"
foo = "foo"


class Controller(GFAction.GFAction):
    zhiyuan = None
    jieshu = None

    def filePath(self):
        return __file__

    def compensateConfig(self):
        dic = self.getMap()
        dic[apl] = (759, 627)
        dic[apr] = (1230, 653)
        dic[hq] = (1530, 542)
        dic[hqe] = (1054, 1037)
        foo = ImageUtil.getImageTemplate("foo")
        self.addCompensateTuple(foo, (1047, 590))

    def step(self):
        assert_exists(ImageUtil.getImageTemplate("3th"), "第三战役")

        self.swipe((1422, 988), (1386, 419), 2)
        self.touch(ImageUtil.getImageTemplate("jzsl"))
        self.touch(ImageUtil.getImageTemplate("normal_battle"))

        self.begin()

        # self.zhiyuan = ImageUtil.getImageTemplate("support_echelon")
        assert_exists(ImageUtil.getImageTemplate("battle_begin"), "开始作战")

        self.sleep(2)

        self.compensate()
        self.addEchelon(apr)
        self.addEchelon(hq)
        self.begin()

        self.supply(apr)
        self.schedule(apr, hqe)
        self.endTurn()
        self.sleepUntilAssert(70, ImageUtil.getImageTemplate("one"))
        self.swipe((1422, 319), (1386, 469), 1)
        self.sleep(1)

        self.endTurn()

        self.sleep(7)
        self.touchBlank()
        self.sleep(3)
        self.touchBlank()
        self.sleep(2)
        self.touchBlank()
        self.sleep(2)
        self.touchBlank()
        self.sleep(2)


c = Controller()
c.run()

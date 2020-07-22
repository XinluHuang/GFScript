import sys

from airtest.core.api import *

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import GFAction
import ImageUtil


class Controller(GFAction.GFAction):
    def filePath(self):
        return __file__

    def compensateConfig(self):
        pass

    def step(self):
        battle_confirm = ImageUtil.getImageTemplate("battle_confirm")
        achievement_settlement = ImageUtil.getImageTemplate("achievement_settlement")
        lfz = ImageUtil.getImageTemplate("lfz")
        v = self.existsFast(lfz)
        v1 = (v[0], v[1] - 40)
        self.touch(v1)
        v2 = self.existsFast(battle_confirm)
        if not v2:
            v = self.existsFast(lfz)
            v1 = (v[0], v[1] - 40)
            self.touch(v1)
            v2 = self.existsFast(battle_confirm)
        self.touch(v2)
        self.sleep(3)
        self.begin()
        self.sleep(5)
        if exists(achievement_settlement):
            self.touchBlank()
        self.sleep(4)


c = Controller()
c.run()

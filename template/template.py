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
        pass


c = Controller()
c.run()

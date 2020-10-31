import os
import Util


class Context:
    rootDir = os.path.dirname(__file__)
    debug = False
    platform = Util.getPlatform()

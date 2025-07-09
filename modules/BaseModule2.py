from core import BaseLoaderClass
from core.module import DModule


class BaseModule2(DModule):
    def run(self): print("BaseModule2.run")
    def onload(self): print("BaseModule2.onload")
    def onunload(self): print("BaseModule2.onunload")


def get_module(loader: BaseLoaderClass):
    return BaseModule2(loader)

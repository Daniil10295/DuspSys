from core import BaseLoaderClass
from core.module import DModule


class BaseModule(DModule):
    def run(self): print("BaseModule.run")
    def onload(self): print("BaseModule.onload")
    def onunload(self): print("BaseModule.onunload")


def get_module(loader: BaseLoaderClass):
    return BaseModule(loader)

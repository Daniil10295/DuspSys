from core import BaseLoaderClass
from core.module import DModule


class BaseModule(DModule):
    def run(self): print("BaseModule.run")


def get_module(loader: BaseLoaderClass):
    return BaseModule(loader)

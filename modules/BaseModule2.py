import time
from core import BaseLoaderClass
from core.module import DModule


class BaseModule2(DModule):
    def run(self, stop_event=None):
        print("BaseModule2.run")
        while not stop_event.is_set():
            print("Работает модуль 2...")
            time.sleep(1)

    def onload(self): print("BaseModule2.onload")
    def onunload(self): print("BaseModule2.onunload")


def get_module(loader: BaseLoaderClass):
    return BaseModule2(loader)

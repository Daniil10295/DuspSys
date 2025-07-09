import time
from core import BaseLoaderClass
from core.module import DModule


class BaseModule(DModule):
    def run(self, stop_event=None):
        print("BaseModule.run")
        while not stop_event.is_set():
            print("Работает модуль...")
            time.sleep(1)

    def onload(self): print("BaseModule.onload")
    def onunload(self): print("BaseModule.onunload")


def get_module(loader: BaseLoaderClass):
    return BaseModule(loader)

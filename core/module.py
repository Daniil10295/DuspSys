from abc import ABC, abstractmethod

class DModule(ABC):
    def __init__(self, loader: "BaseLoaderClass"):
        self.loader = loader

    @abstractmethod
    def run(self): pass

    def onload(self): pass
    def onunload(self): pass
    def start(self): self.run()
    def stop(self): pass
    def is_running(self): return False
from abc import abstractmethod
from .baseLoader import BaseLoaderClass

__all__ = ['DModule', 'thread_safe']


def thread_safe(func):
    def wrapper(*args, **kwargs):
        import threading
        threading.Thread(target=func, args=args, kwargs=kwargs, daemon=True).start()
    return wrapper


class DModule:
    loader: BaseLoaderClass
    data_dir: str
    name: str

    def __init__(self, loader: BaseLoaderClass):
        self.loader = loader
        self.name = self.__class__.__name__
        self.data_dir = loader.get_data_dir(self.name)

    @abstractmethod
    def run(self): raise NotImplementedError("Module must implement run method")

    def save_data(self, name, data):
        return self.loader.save_data(name, data, self.name)

    def load_data(self, name):
        return self.loader.load_data(name, self.name)

    def delete_data(self, name):
        return self.loader.delete_data(name, self.name)

    def onload(self): pass
    def onunload(self): pass

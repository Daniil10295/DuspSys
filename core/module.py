from abc import abstractmethod

__all__ = ['DModule']


class DModule:
    from core.baseLoader import BaseLoaderClass
    loader: BaseLoaderClass
    data_dir: str

    def __init__(self, loader: BaseLoaderClass):
        self.loader = loader
        self.data_dir = loader.get_data_dir(__class__.__name__)

    @abstractmethod
    def run(self): raise NotImplementedError("Module must implement run method")

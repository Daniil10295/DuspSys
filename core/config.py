from pathlib import Path

from core import BaseLoaderClass

__all__ = ['DuspConfig']


class DuspConfig:
    __vars = ("loader", "ignore_errors", "data_ric", "modules_path", "loaders_path", "data_path")
    loader: BaseLoaderClass
    ignore_errors: bool
    data_ric: dict = {  ## Reinstall core
        "mode_ric": False,
        "ric_folder": "",
    }
    modules_path: Path
    loaders_path: Path
    data_path: Path

    def __init__(self, config: dict):
        for var in self.__vars:
            setattr(self, var, config.get(var, getattr(self, var)))

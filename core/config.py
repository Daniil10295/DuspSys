import os
import sys
from pathlib import Path

__all__ = ['DuspConfig']


class DuspConfig:
    __vars = ("loader", "ignore_errors", "data_ric", "modules_path", "loaders_path", "data_path")
    loader: "BaseLoaderClass" = None
    ignore_errors: bool = False
    data_ric: dict = {  ## Reinstall core
        "mode_ric": False,
        "ric_folder": "",
    }
    base_path: Path = Path(__file__).parent.parent
    modules_path: Path = base_path / "modules"
    loaders_path: Path = base_path / "loaders"
    data_path: Path = base_path / "data"

    def __init__(self, config: dict):
        for var in [self.base_path, self.modules_path, self.loaders_path, self.data_path, self.base_path / "core"]:
            sys.path.insert(0, os.path.dirname(var))
        for var in self.__vars:
            setattr(self, var, config.get(var, getattr(self, var)))

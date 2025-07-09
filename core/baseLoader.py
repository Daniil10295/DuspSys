import os
import importlib
from pathlib import Path

from .config import DuspConfig
from .exeptions import *


__all__ = ['BaseLoaderClass', 'get_module']

def get_module(module_path: Path):
    module = importlib.import_module("modules." + os.path.splitext(os.path.basename(module_path))[0])
    module.__name__ = module_path.name.removesuffix(".py")
    return module


class BaseLoaderClass:
    modules: dict[str, "DModule"] = {}

    def __init__(self, config: DuspConfig):
        self.config = config

    def get_data_dir(self, module_name: str) -> str:
        return os.path.join(self.config.data_path, module_name)

    def load_module(self, module_name: str):
        if module_name in self.modules:
            raise ModuleAlreadyLoadedException(module_name)
        module = get_module(self.config.modules_path / Path(module_name + ".py"))
        self.modules[module_name] = module.get_module(self)
        self.modules[module_name].onload()
        return module

    def load_modules(self):
        for module_file in os.listdir(self.config.modules_path):
            if module_file in self.modules:
                continue
            if module_file.startswith("__"):
                continue
            if module_file.endswith(".py"):
                self.load_module(module_file[:-3])

    def unload_module(self, module_name: str):
        self.modules.pop(module_name).onunload()

    def unload_modules(self):
        for name in list(self.modules.keys()):
            self.unload_module(name)

    def get_module(self, module_name: str):
        module =  self.modules.get(module_name, None)
        if module is None:
            module = self.load_module(module_name)
        if module is None:
            raise ModuleNotFoundException(module_name)
        return module

    def run_module(self, module_name: str):
        module = self.get_module(module_name)
        module.run()


    def run_all_modules(self):
        for name, module in self.modules.items():
            self.run_module(name)

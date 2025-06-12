import os
from core import *

__all__ = ['BaseLoaderClass', 'get_module']

def get_module(module_file):
    module = __import__("modules." + module_file)
    return module


class BaseLoaderClass:
    modules: list[DModule] = {}

    def __init__(self, config: DuspConfig):
        self.config = config

    def get_data_dir(self, module_name: str) -> str:
        return os.path.join(self.config.data_path, module_name)

    def load_module(self, module_name: str):
        module = get_module(module_name)
        self.modules[module_name] = module.get_module(self)
        return module

    def load_modules(self):
        for module in os.listdir(self.config.modules_path):
            self.load_module(module)

    def unload_modules(self):
        self.modules = []

    def run_module(self, module_name: str):
        module = self.load_module(module_name)

    def run_all_modules(self):
        for module in self.modules:
            self.modules[module].run()

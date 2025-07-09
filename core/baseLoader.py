import threading
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
    module_threads: dict[str, threading.Thread] = {}
    stop_events: dict[str, threading.Event] = {}

    def __init__(self, config: DuspConfig):
        self.config = config

    def get_data_dir(self, module_name: str) -> str:
        return os.path.join(self.config.data_path, module_name)

    def load_module(self, module_name: str):
        if module_name in self.modules:
            raise ModuleAlreadyLoadedException(module_name)
        module = get_module(self.config.modules_path / Path(module_name + ".py"))
        instance = module.get_module(self)
        self.modules[module_name] = instance
        self.stop_events[module_name] = threading.Event()
        instance.onload()
        return instance

    def load_modules(self):
        for module_file in os.listdir(self.config.modules_path):
            if module_file.startswith("__") or not module_file.endswith(".py"):
                continue
            module_name = module_file[:-3]
            if module_name not in self.modules:
                self.load_module(module_name)

    def unload_module(self, module_name: str):
        if module_name in self.modules:
            # Сигнал остановки
            if module_name in self.stop_events:
                self.stop_events[module_name].set()

            # Ожидание завершения потока
            thread = self.module_threads.get(module_name)
            if thread and thread.is_alive():
                thread.join(timeout=5)

            self.modules[module_name].onunload()
            del self.modules[module_name]
            self.module_threads.pop(module_name, None)
            self.stop_events.pop(module_name, None)

    def unload_modules(self):
        for name in list(self.modules.keys()):
            self.unload_module(name)

    def get_module(self, module_name: str):
        module = self.modules.get(module_name, None)
        if module is None:
            module = self.load_module(module_name)
        return module

    def run_module(self, module_name: str):
        module = self.get_module(module_name)
        stop_event = self.stop_events[module_name]

        def module_runner():
            try:
                module.run(stop_event)
            except Exception as e:
                print(f"Module {module_name} crashed: {e}")

        thread = threading.Thread(target=module_runner, name=f"ModuleThread-{module_name}", daemon=True)
        self.module_threads[module_name] = thread
        thread.start()

    def run_all_modules(self):
        for name in self.modules.keys():
            self.run_module(name)

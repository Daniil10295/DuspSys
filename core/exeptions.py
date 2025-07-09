__all__ = ['ModuleNotFoundException', 'ModuleNotLoadedException', 'ModuleAlreadyLoadedException']

class ModuleException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class ModuleAlreadyLoadedException(ModuleException):
    def __init__(self, module_name: str):
        super().__init__(f"Module {module_name} is already loaded")


class ModuleNotLoadedException(ModuleException):
    def __init__(self, module_name: str):
        super().__init__(f"Module {module_name} is not loaded")


class ModuleNotFoundException(ModuleException):
    def __init__(self, module_name: str):
        super().__init__(f"Module {module_name} not found")

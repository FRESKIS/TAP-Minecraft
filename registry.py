# registry.py
import pkgutil, importlib, inspect
from agents.BaseAgent import BaseAgent

def discover_agents():
    registry = {}
    package = importlib.import_module("agents")

    for _, module_name, _ in pkgutil.iter_modules(package.__path__, "agents."):
        module = importlib.import_module(module_name)
        for _, cls in inspect.getmembers(module, inspect.isclass):
            if issubclass(cls, BaseAgent) and cls is not BaseAgent:
                registry[cls.__name__] = cls
    return registry

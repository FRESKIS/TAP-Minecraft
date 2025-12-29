from abc import ABC, abstractmethod

class base(ABC):
    @abstractmethod
    def build(self, mc, pos):
        pass
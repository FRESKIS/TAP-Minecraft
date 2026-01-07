from abc import ABC, abstractmethod

class miner_strategie(ABC):
    @abstractmethod
    def mine():
        pass

class vertical(miner_strategie):
    def mine():
        pass

class Layer(miner_strategie):
    def mine():
        pass
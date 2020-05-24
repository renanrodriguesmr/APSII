from abc import ABC, abstractmethod

class AbstractDataset(ABC):
    """
    Each distinct dataset class should have a base interface. A singleton class.
    """

    @staticmethod
    @abstractmethod
    def getInstance(self):
        pass

    @abstractmethod
    def _preProcess(self):
        pass
from abc import ABC, abstractmethod

class DatasetAbstractFactory(ABC):
    """
    Abstract interface to declares a method to return
    the abstract product, a singleton to provide the preprocessed datataset
    """
    
    @abstractmethod
    def getDataset(self):
        pass
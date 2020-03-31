from abc import ABC, abstractmethod
from src.models.saeb_2011 import SAEB2011

class DatasetAbstractFactory(ABC):
    """
    Abstract interface to declares a method to return
    the abstract product, a singleton to provide the preprocessed datataset
    """
    
    @abstractmethod
    def getDataset(self):
        pass

class Factory_SAEB_2011(DatasetAbstractFactory):
    """
    Concrete factory to produce a singleton to provide the 
    preprocessed datataset of SAEB_2011
    """
    def getDataset(self):
        return SAEB2011.getInstance()
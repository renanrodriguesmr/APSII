from abc import ABC, abstractmethod
from src.models.escolas import Escolas

class DatasetAbstractFactory(ABC):
    """
    Abstract interface to declares a method to return
    the abstract product, a singleton to provide the preprocessed datataset
    """
    
    @abstractmethod
    def getDataset(self):
        pass

class Factory_Escolas(DatasetAbstractFactory):
    """
    Concrete factory to produce a singleton to provide the 
    preprocessed datataset of Escolas
    """
    def getDataset(self):
        return Escolas.getInstance().data
from abc import ABC, abstractmethod
from src.models.escolas import Escolas
from src.models.ideb_brasil import IDEBBrasil
from src.models.ideb_escolas import IDEBEscolas

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

class Factory_IDEBBrasil(DatasetAbstractFactory):
    """
    Concrete factory to produce a singleton to provide the 
    preprocessed datataset of IDEBBrasil
    """
    def getDataset(self):
        return IDEBBrasil.getInstance().data

class Factory_IDEBEscolas(DatasetAbstractFactory):
    """
    Concrete factory to produce a singleton to provide the 
    preprocessed datataset of IDEBEscolas
    """
    def getDataset(self):
        return IDEBEscolas.getInstance().data
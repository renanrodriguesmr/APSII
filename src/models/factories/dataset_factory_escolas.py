from src.models.escolas import Escolas
from src.models.factories.dataset_factory_abstract import DatasetAbstractFactory

class Factory_Escolas(DatasetAbstractFactory):
    """
    Concrete factory to produce a singleton to provide the 
    preprocessed datataset of Escolas
    """
    def getDataset(self):
        return Escolas.getInstance().data
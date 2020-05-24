from src.models.factories.dataset_factory_abstract import DatasetAbstractFactory
from src.models.ideb_escolas import IDEBEscolas

class Factory_IDEBEscolas(DatasetAbstractFactory):
    """
    Concrete factory to produce a singleton to provide the 
    preprocessed datataset of IDEBEscolas
    """
    def getDataset(self):
        return IDEBEscolas.getInstance().data
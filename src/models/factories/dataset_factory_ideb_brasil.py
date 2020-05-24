from src.models.factories.dataset_factory_abstract import DatasetAbstractFactory
from src.models.ideb_brasil import IDEBBrasil

class Factory_IDEBBrasil(DatasetAbstractFactory):
    """
    Concrete factory to produce a singleton to provide the 
    preprocessed datataset of IDEBBrasil
    """
    def getDataset(self):
        return IDEBBrasil.getInstance().data
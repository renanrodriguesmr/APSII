from src.models.factories.dataset_factory_escolas import Factory_Escolas
from src.models.factories.dataset_factory_ideb_brasil import Factory_IDEBBrasil
from src.models.factories.dataset_factory_ideb_escolas import Factory_IDEBEscolas

class Setup():

    @staticmethod
    def processData():
        f = Factory_IDEBBrasil()
        f.getDataset()

        f = Factory_IDEBEscolas()
        f.getDataset()

        f = Factory_Escolas()
        f.getDataset()
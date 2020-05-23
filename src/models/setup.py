from src.models.dataset_factories import Factory_Escolas, Factory_IDEBBrasil, Factory_IDEBEscolas

class Setup():

    @staticmethod
    def processData():
        f = Factory_IDEBBrasil()
        f.getDataset()

        f = Factory_IDEBEscolas()
        f.getDataset()

        f = Factory_Escolas()
        f.getDataset()
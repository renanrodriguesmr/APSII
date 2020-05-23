from src.models.dataset_factories import Factory_Escolas

class Setup():

    @staticmethod
    def processData():
        f = Factory_Escolas()
        f.getDataset()
from src.models.factories.dataset_factory_escolas import Factory_Escolas
from src.models.setup import Setup

Setup.processData()

f = Factory_Escolas()
instance = f.getDataset()
print(instance.iloc[0])

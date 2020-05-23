from src.models.dataset_factories import Factory_Escolas
from src.models.setup import Setup

Setup.processData()

f = Factory_Escolas()
instance = f.getDataset()
print(instance.head())

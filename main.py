from src.models.dataset_factories import Factory_IDEBBrasil
from src.models.setup import Setup

Setup.processData()

f = Factory_IDEBBrasil()
instance = f.getDataset()
print(instance.head())

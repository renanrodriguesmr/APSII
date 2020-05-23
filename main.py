from src.models.dataset_factories import Factory_IDEBEscolas
from src.models.setup import Setup

Setup.processData()

f = Factory_IDEBEscolas()
instance = f.getDataset()
print(instance.head())

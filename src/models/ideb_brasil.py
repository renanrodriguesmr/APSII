from src.models.abstract_dataset import AbstractDataset
from src.models.settings import DATA_DIRECTORY, IDEBBrasil_CSV
import pandas as pd

class IDEBBrasil(AbstractDataset):
    __instance = None

    def __init__(self):
    #Virtually private constructor.
      if IDEBBrasil.__instance != None:
        raise Exception("This class is a singleton!")
      else:
        self._preProcess()
        IDEBBrasil.__instance = self
    
    @staticmethod
    def getInstance():
    #Static access method.
        if IDEBBrasil.__instance == None:
            IDEBBrasil()
        return IDEBBrasil.__instance
    
    def _preProcess(self):
        print("Lendo dados do ideb brasil 2015...")
        path = DATA_DIRECTORY + IDEBBrasil_CSV 
        self.data = pd.read_csv(path, sep="|", header=0)

from src.models.abstract_dataset import AbstractDataset
from src.models.settings import DATA_DIRECTORY, ESCOLAS_CSV
import pandas as pd

class Escolas(AbstractDataset):
    __instance = None

    def __init__(self):
    #Virtually private constructor.
      if Escolas.__instance != None:
        raise Exception("This class is a singleton!")
      else:
        self._preProcess()
        Escolas.__instance = self
    
    @staticmethod
    def getInstance():
    #Static access method.
        if Escolas.__instance == None:
            Escolas()
        return Escolas.__instance
    
    def _preProcess(self):
        print("Lendo dados do censo")
        path = DATA_DIRECTORY + ESCOLAS_CSV 
        self.data = pd.read_csv(path, sep="|", header=0, engine='python')

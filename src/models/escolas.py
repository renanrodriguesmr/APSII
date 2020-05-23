from src.models.abstract_dataset import AbstractDataset
import pandas as pd

class Escolas(AbstractDataset):
    __instance = None
    path = "data/ESCOLAS.CSV"

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
        df = pd.read_csv(self.path, sep="|", header=0, engine='python')
        self.data = df

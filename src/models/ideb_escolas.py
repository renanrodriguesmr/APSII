from src.models.abstract_dataset import AbstractDataset
from src.models.settings import DATA_DIRECTORY, IDEBEscolas_EXCEL
import pandas as pd

class IDEBEscolas(AbstractDataset):
    __instance = None

    def __init__(self):
    #Virtually private constructor.
      if IDEBEscolas.__instance != None:
        raise Exception("This class is a singleton!")
      else:
        self._preProcess()
        IDEBEscolas.__instance = self
    
    @staticmethod
    def getInstance():
    #Static access method.
        if IDEBEscolas.__instance == None:
            IDEBEscolas()
        return IDEBEscolas.__instance
    
    def _preProcess(self):
        print("Lendo dados do ideb escolas 2015...")
        path = DATA_DIRECTORY + IDEBEscolas_EXCEL 
        self.data = pd.read_excel(path, sheet_name="IDEB_Escolas", header=0)

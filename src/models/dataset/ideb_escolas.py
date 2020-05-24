from src.models.dataset.abstract_dataset import AbstractDataset
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
        cols_to_use = ["cod_escola", "Aprov_6_9", "Aprov_6", "Aprov_7", "Aprov_8", "Aprov_9"]
        dtype_to_use = {"cod_escola": "Int64", "Aprov_6_9": "float64", "Aprov_6": "float64", "Aprov_7": "float64", "Aprov_8": "float64", "Aprov_9": "float64"}
        na_values_list = ['-']

        self.data = pd.read_excel(path, sheet_name="IDEB_Escolas", decimal=",", header=0, usecols=cols_to_use, dtype=dtype_to_use, na_values=na_values_list)

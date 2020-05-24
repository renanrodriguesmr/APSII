from src.models.dataset.abstract_dataset import AbstractDataset
from src.models.factories.dataset_factory_ideb_escolas import Factory_IDEBEscolas
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
        
        cols_to_use = ["CO_ENTIDADE", "CO_REGIAO", "CO_UF", "TP_DEPENDENCIA", "TP_LOCALIZACAO", "IN_AGUA_FILTRADA", "IN_ENERGIA_INEXISTENTE", "IN_QUADRA_ESPORTES", "IN_BIBLIOTECA_SALA_LEITURA", "IN_AREA_VERDE", "IN_INTERNET", "IN_ALIMENTACAO", "TP_AEE", "TP_ATIVIDADE_COMPLEMENTAR", "IN_FUNDAMENTAL_CICLOS", "IN_FINAL_SEMANA", "IN_MEDIACAO_PRESENCIAL", "IN_ESP_EXCLUSIVA_FUND_AF"]
        dtype_to_use = {"CO_ENTIDADE": "Int64", "CO_REGIAO": "Int64", "CO_UF": "Int64", "TP_DEPENDENCIA": "Int64", "TP_LOCALIZACAO": "Int64", "IN_AGUA_FILTRADA": "Int64", "IN_ENERGIA_INEXISTENTE": "Int64", "IN_QUADRA_ESPORTES": "Int64", "IN_BIBLIOTECA_SALA_LEITURA": "Int64", "IN_AREA_VERDE": "Int64", "IN_INTERNET": "Int64", "IN_ALIMENTACAO": "Int64", "TP_AEE": "Int64", "TP_ATIVIDADE_COMPLEMENTAR": "Int64", "IN_FUNDAMENTAL_CICLOS": "Int64", "IN_FINAL_SEMANA": "Int64", "IN_MEDIACAO_PRESENCIAL": "Int64", "IN_ESP_EXCLUSIVA_FUND_AF": "Int64"}
        na_values_list = ['']

        df_censo = pd.read_csv(path, sep="|", header=0, engine='python', usecols=cols_to_use, dtype=dtype_to_use, na_values=na_values_list)

        factory = Factory_IDEBEscolas()
        df_ideb = factory.getDataset()

        df_escolas = pd.merge(df_censo, df_ideb, left_on='CO_ENTIDADE', right_on='cod_escola', how='inner')

        self.data = df_escolas

from src.models.abstract_dataset import AbstractDataset

class SAEB2011(AbstractDataset):
    __instance = None

    def __init__(self):
    #Virtually private constructor.
      if SAEB2011.__instance != None:
        raise Exception("This class is a singleton!")
      else:
        self._preProcess()
        SAEB2011.__instance = self
    
    @staticmethod
    def getInstance():
    #Static access method.
        if SAEB2011.__instance == None:
            SAEB2011()
        return SAEB2011.__instance
    
    def _preProcess(self):
        print("aaaa")

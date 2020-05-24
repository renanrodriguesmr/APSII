import pandas as pd
from src.usecases.question import Question
from src.models.factories.dataset_factory_ideb_brasil import Factory_IDEBBrasil

class Question3(Question):
    def ask(self):
        print("Pergunta 3 : A taxa de reprovação aumenta ao longo do ensino fundamental?")

    def answer(self):
        factory = Factory_IDEBBrasil()
        df = factory.getDataset()
        rates = self.__getDictOfRate(df)
        rates = self.__sortRates(rates)
        print("\nAs taxas de reprovação seguem em ordem decrescente:\n")

        for rate in rates:
            print(rate[0], rate[1])

    def __getRateBySerie(self, value, df):
        index = value - 4
        return df.iloc[0].iloc[index]

    def __getDictOfRate(self, df):
        ano_6 = self.__getRateBySerie(6, df)
        ano_7 = self.__getRateBySerie(7, df)
        ano_8 = self.__getRateBySerie(8, df)
        ano_9 = self.__getRateBySerie(9, df)

        return {
            "6 ano": ano_6,
            "7 ano": ano_7,
            "8 ano": ano_8,
            "9 ano": ano_9
        }
    
    def __sortRates(self, rates):
        return sorted(rates.items(), key = lambda x: x[1])
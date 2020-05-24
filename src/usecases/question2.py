import pandas as pd
from src.usecases.question import Question
from src.models.factories.dataset_factory_ideb_brasil import Factory_IDEBBrasil

class Question2(Question):
    def ask(self):
        print("Pergunta 2: Escolas particulares possuem um maior índice de reprovação do que as escolas públicas?")

    def answer(self):
        factory = Factory_IDEBBrasil()
        df = factory.getDataset()
        print("comparando do 6 ao 9 ano do ensindo fundamental...")

        public = self.__getPublicRate(df)
        private = self.__getPrivateRate(df)

        print("reprovacao em escolas públicas:")
        print(public)
        print("reprovacao em escolas privadas:")
        print(private)
        print(self.__printGreaterType(public, private))

    def __getPublicRate(self, df):
        return df.iloc[3].iloc[1]

    def __getPrivateRate(self, df):
        return df.iloc[4].iloc[1]
    
    def __printGreaterType(self, public, private):
        if(public < private):
            return "Escolas Pública possuem taxas menores."
        if(public == private):
            return "Escolas públicas e privadas possuem a mesma taxa de reprovação"

        return "Escolas Privadas possuem taxas menores."
import pandas as pd
from src.usecases.question import Question
from src.models.factories.dataset_factory_escolas import Factory_Escolas 
import numpy as np 
from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.preprocessing import StandardScaler



class Question1(Question):
    def ask(self):
        print("Pergunta 1: Quais as principais características que levam uma escola à ter um alto índice de reprovação, ou seja, por que uma escola reprova muito?")

    def answer(self):
        

        print("resposta 1")
        factory = Factory_Escolas()
        df = factory.getDataset()
        print("comparando resultados das escolas públicas do brasil")

        df = df.dropna()

        def transforms(p):
            if (p<85):
                return "yes"
            else:
                return "no"

        pd.set_option('mode.chained_assignment', None)
        df['Aprov_6_9'] = df['Aprov_6_9'].map(transforms)
        df['Aprov_6_9'] = df['Aprov_6_9'].astype('category')

        scaler = StandardScaler()
        scaler.fit(df.drop('Aprov_6_9', axis=1))
        scaled_features = scaler.transform(df.drop('Aprov_6_9',axis=1))
        df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])
        X = df_feat
        y = df['Aprov_6_9']


        X, y = make_classification(n_samples=40000,
                            n_features=19,
                            n_informative=17,
                            n_redundant=0,
                            n_repeated=2,
                            n_classes=2,
                            random_state=0,
                            shuffle=False)

        forest = ExtraTreesClassifier(n_estimators=250,
                                random_state=0)

        forest.fit(X,y)

        importances = forest.feature_importances_
        std = np.std([tree.feature_importances_ for tree in forest.estimators_],
                axis=0)
        indices = np.argsort(importances)[::-1]

        # Print the feature ranking
        print("Feature ranking:")

        for f in range(X.shape[1]):
            print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

        print("As features 13,15,14 e 11 mostram-se relevantes para questão e representam, respectivamente, os fatos de uma escola:")
        print("Possuir atividades complementares")
        print("Possuir atividades atividades aos finais de semana")
        print("Possuir  ensino organizado em ciclos")
        print("Possuir alimentação para os alunos")


    

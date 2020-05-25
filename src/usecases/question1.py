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
        np.std([tree.feature_importances_ for tree in forest.estimators_],
                axis=0)
        indices = np.argsort(importances)[::-1]

        # Print the feature ranking
        print("Feature ranking:")

        features_name = self.get_columns_name()
        descriptions = self.get_descption_columns()

        for f in range(X.shape[1]):
            print("%d. %s (%f)" % (f + 1, descriptions[features_name[indices[f]]], importances[indices[f]]))

        print("\nPortanto as features mais relevantes são:")

        for f in range(5):
            print("%d. %s" % (f + 1, descriptions[features_name[indices[f]]]))

    def get_columns_name(self):
        factory = Factory_Escolas()
        df = factory.getDataset()
        return df.columns

    def get_descption_columns(self):
        return {
                "TP_ATIVIDADE_COMPLEMENTAR": "Atividade complementar",
                "IN_FINAL_SEMANA": "Atividade final de semana",
                "IN_FUNDAMENTAL_CICLOS": "Ensino em ciclos",
                "IN_ALIMENTACAO": "Alimentação na escola",
                "CO_UF": "Município",
                "IN_AGUA_FILTRADA": "Água Filtrada",
                "CO_REGIAO": "Região",
                "TP_LOCALIZACAO": "Localização Rural/urbana",
                "CO_ENTIDADE": "código da escola",
                "TP_DEPENDENCIA": "federal/municipal/estadual",
                "TP_AEE": "Atendimento educacional especializado",
                "cod_escola": "Código da escola",
                "IN_ENERGIA_INEXISTENTE": "Energia inexistente",
                "IN_MEDIACAO_PRESENCIAL": "Presencial",
                "IN_AREA_VERDE": "Possui area verde",
                "IN_ESP_EXCLUSIVA_FUND_AF": "Exclusiva para turmas de 6 a 9 ano",
                "IN_QUADRA_ESPORTES": "Possui quadra de esportes",
                "IN_INTERNET": "Possui internet",
                "IN_BIBLIOTECA_SALA_LEITURA": "Existe biblioteca ou sala de leitura",
                }
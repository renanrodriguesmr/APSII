from src.models.setup import Setup
from src.usecases.question1 import Question1
from src.usecases.question2 import Question2
from src.usecases.question3 import Question3
from src.models.factories.dataset_factory_escolas import Factory_Escolas
import numpy as np 
from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd



def getQuestions():
    print("\n\n======= Perguntas =======\n")
    q1 = Question1()
    q2 = Question2()
    q3 = Question3()

    q1.ask()
    q2.ask()
    q3.ask()

    return {"1": q1, "2": q2, "3": q3}

def transforms(p):
    if (p<85):
        return "yes"
    else:
        return "no"

if __name__ == "__main__":
    Setup.processData()
    
     questions = getQuestions()

    value = input('\nEscolha uma pergunta: ')

    q = questions[value]
    q.answer()


   

    



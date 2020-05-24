from src.models.setup import Setup
from src.usecases.question1 import Question1
from src.usecases.question2 import Question2
from src.usecases.question3 import Question3

def getQuestions():
    print("\n\n======= Perguntas =======\n")
    q1 = Question1()
    q2 = Question2()
    q3 = Question3()

    q1.ask()
    q2.ask()
    q3.ask()

    return {"1": q1, "2": q2, "3": q3}

def handle_input(value, questions):
    if(value not in questions):
        print("Pergunta não existente.")
    else:
        q = questions[value]
        q.answer()

if __name__ == "__main__":
    Setup.processData()
    questions = getQuestions()
    value = input('\nEscolha uma pergunta: ')
    handle_input(value, questions)
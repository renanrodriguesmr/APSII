from src.usecases.question import Question

class Question2(Question):
    def ask(self):
        print("Pergunta 2: Escolas particulares possuem um maior índice de reprovação do que as escolas públicas?")

    def answer(self):
        print("resposta 2")
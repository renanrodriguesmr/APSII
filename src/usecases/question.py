from abc import ABC, abstractmethod


class Question(ABC):
    
    @abstractmethod
    def answer(self):
        pass

    @abstractmethod
    def ask(self):
        pass
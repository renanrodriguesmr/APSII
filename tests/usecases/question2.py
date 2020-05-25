from src.usecases.question2 import Question2
import io
import unittest
import unittest.mock


class TestQuestion2Methods(unittest.TestCase):
    def test__printGreaterType_greater(self):
        q2 = Question2()
        self.assertEqual(q2._Question2__printGreaterType(5, 10), "Escolas Pública possuem taxas maiores de reprovação.")
    
    def test__printGreaterType_equal(self):
        q2 = Question2()
        self.assertEqual(q2._Question2__printGreaterType(5, 5), "Escolas públicas e privadas possuem a mesma taxa de reprovação")
    
    def test__printGreaterType_less(self):
        q2 = Question2()
        self.assertEqual(q2._Question2__printGreaterType(10, 5), "Escolas Privadas possuem taxas maiores de reprovação.")
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_ask(self, mock_stdout=""):
        q2 = Question2()
        q2.ask()
        self.assertEqual(mock_stdout.getvalue(), 'Pergunta 2: Escolas particulares possuem um maior índice de reprovação do que as escolas públicas?\n')

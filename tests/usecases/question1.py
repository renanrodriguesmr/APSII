from src.usecases.question1 import Question1
import io
import unittest
import unittest.mock


class TestQuestion1Methods(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_ask(self, mock_stdout=""):
        q1 = Question1()
        q1.ask()
        self.assertEqual(mock_stdout.getvalue(), 'Pergunta 1: Quais as principais características que levam uma escola à ter um alto índice de reprovação, ou seja, por que uma escola reprova muito?\n')

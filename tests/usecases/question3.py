from src.usecases.question3 import Question3
import io
import unittest
import unittest.mock


class TestQuestion3Methods(unittest.TestCase):
    def test__sortRates_sorted(self):
        q3 = Question3()
        self.assertEqual(q3._Question3__sortRates({"1": 1,"2": 2}), [('1', 1), ('2', 2)])
    
    def test__sortRates_unsorted(self):
        q3 = Question3()
        self.assertEqual(q3._Question3__sortRates({"2": 2,"1": 1}), [('1', 1), ('2', 2)])
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_ask(self, mock_stdout=""):
        q3 = Question3()
        q3.ask()
        self.assertEqual(mock_stdout.getvalue(), 'Pergunta 3 : A taxa de reprovação aumenta ao longo do ensino fundamental?\n')

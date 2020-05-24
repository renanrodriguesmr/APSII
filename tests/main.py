from main import handle_input
import io
import unittest
import unittest.mock


class TestMain(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, expected_output, mock_stdout=""):
        handle_input(4, {"1": "", "2": "", "3": ""})
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_nonexistent_question(self):
        self.assert_stdout('Pergunta não existente.\n')
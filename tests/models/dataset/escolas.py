from src.models.dataset.escolas import Escolas
import io
import unittest
import unittest.mock


class TestEscolasDataSet(unittest.TestCase):
  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def test_getinstance(self, mock_stdout=""):
    data = Escolas.getInstance()
    self.assertIsInstance(data, Escolas)
from src.models.dataset.ideb_escolas import IDEBEscolas
import io
import unittest
import unittest.mock


class TestIDEBEscolasDataSet(unittest.TestCase):
  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def test_getinstance(self, mock_stdout=""):
    data = IDEBEscolas.getInstance()
    self.assertIsInstance(data, IDEBEscolas)
from src.models.dataset.ideb_brasil import IDEBBrasil
import io
import unittest
import unittest.mock


class TestIDEBBrasilDataSet(unittest.TestCase):
  @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
  def test_getinstance(self, mock_stdout=""):
    data = IDEBBrasil.getInstance()
    self.assertIsInstance(data, IDEBBrasil)
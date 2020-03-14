from Zadanie4 import *
import io
import unittest
import unittest.mock

class TestXor(unittest.TestCase):
    """Test xor function"""

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_xor(self, mock_stdout):
        xor("Python", 7)
        self.assertEqual(mock_stdout.getvalue(), "W~sohi\n")



class TestDexor(unittest.TestCase):
    """Test dexor function"""

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_dexor(self, mock_stdout):
        dexor("W~sohi", 7)
        self.assertEqual(mock_stdout.getvalue(), "Python\n")


if __name__ == "__main__":
    unittest.main()

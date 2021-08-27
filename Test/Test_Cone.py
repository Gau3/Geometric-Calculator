import unittest
from Cone_Area import cone_volume

class TestVolume(unittest.TestCase):
    def test_list_int(self):
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result, 6)
if __name__ == '__main__':
    unittest.main()
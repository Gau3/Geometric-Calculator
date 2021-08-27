import unittest
from Cylinder_Area_Volume import cylinder_area

class TestArea(unittest.TestCase):
    def test_list_int(self):
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result, 6)
if __name__ == '__main__':
    unittest.main()

import unittest
from Cylinder_Area_Volume import cylinder_volume

class TestVolume(unittest.TestCase):
    def test_list_int(self):
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result, 6)
if __name__ == '__main__':
    unittest.main()
    
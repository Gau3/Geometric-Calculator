import unittest
from Rectangle import rectangle_perimeter

class TestPerimeter(unittest.TestCase):
    def test_list_int(self):
        data = [1,2]
        result = sum(data)
        self.assertEqual(result, 3)
if __name__ == '__main__':
    unittest.main()
    
from Rectangle import rectangle_area

class TestArea(unittest.TestCase):
    def test_list_int(self):
        data = [1,2]
        result =sum(data)
        self.assertEqual(result, 3)
if __name__ == '__main__':
    unittest.main()
    
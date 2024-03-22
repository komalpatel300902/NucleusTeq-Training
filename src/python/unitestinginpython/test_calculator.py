import unittest
import calculator
class TestClaculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This is from setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("This is from setDownClass")

    def setUp(self) -> None:
        print("This is setUp")
        self.c = calculator.Calculator()
    def tearDown(self) -> None:
        print("This is tearDown")

    def test_add(self):
        self.assertEqual(self.c.add(12,23),35)
        self.assertEqual(self.c.add(14,-13),1)
        self.assertEqual(self.c.add(-1,-34),-35)

    def test_subtract(self):
        self.assertEqual(self.c.subtract(12,45),-33)
        self.assertEqual(self.c.subtract(90,-15),105)
        self.assertEqual(self.c.subtract(-12,-45),33)

if __name__ == "__main__":
    unittest.main()
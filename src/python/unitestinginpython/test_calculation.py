import unittest
import calculation as c

class TestingCalculation(unittest.TestCase):


    def test_add(self):
        self.assertEqual(c.add([12,-23,0]),-11)
        
        

    def test_avg(self):
        self.assertEqual(c.average([12,24,12]),16)
        

    def test_sum_n(self): 
        self.assertEqual(c.first_n_natural_number(4),10)
        


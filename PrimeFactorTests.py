import unittest
from  PrimeFactor import *


class PrimeFactorTest(unittest.TestCase):
    def test_None(self):
        ans  = None
        with self.assertRaises(Exception):
            PrimeFactor(ans)
    
    def test_zero(self):
        ans  = 0
        with self.assertRaises(Exception):
            PrimeFactor(ans)

    def test_negative(self):
        ans  = -23
        with self.assertRaises(Exception):
            PrimeFactor(ans) 

    def test_float(self):
        ans  = 1.0
        self.assertEqual([],PrimeFactor(ans))
            
    def test_two(self):
        ans  = 4
        self.assertEqual([2,2],PrimeFactor(ans))

    def test_four(self):
        ans  = 8
        self.assertEqual([2,2,2],PrimeFactor(ans))

    def test_complex(self):
        ans  = 2*2*3*3*7*5*11*11*13*17
        self.assertEqual([2,2,3,3,5,7,11,11,13,17],PrimeFactor(ans))

if __name__ == '__main__':
    unittest.main()


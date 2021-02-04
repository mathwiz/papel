import asciicode
import unittest
import random

protein = "ACTIN"
A = '1000001'
C = '1000011'
T = '1010100'
I = '1001001'
N = '1001110'

class TestCase1(unittest.TestCase):
    def test1(self):
        coded = asciicode.binary_list(protein)
        self.assertEqual(coded[0], A)
        self.assertEqual(coded[1], C)
        self.assertEqual(coded[2], T)
        self.assertEqual(coded[3], I)
        self.assertEqual(coded[4], N)

    def test2(self):
        self.assertEqual(asciicode.binary(protein), "".join([A,C,T,I,N]))




if __name__ == '__main__':
    unittest.main()

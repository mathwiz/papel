import asciicode
import unittest
import random

protein = "ACTIN"


class TestCase1(unittest.TestCase):
    def test1(self):
        print(protein)
        for x in protein:
            coded = 1
            print(x + '->' + coded)




if __name__ == '__main__':
    unittest.main()

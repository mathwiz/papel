import code
import unittest
import random

alpha = 'ABCDEFGHIJKLMNOPQRST'

class TestCase1(unittest.TestCase):
    def test2(self):
        print(len(alpha))
        for x in range(10):
            x = random.randint(0,len(alpha)-1)
            letter = alpha[x]
            coded = code.rot13(letter)
            print(letter + '->' + coded)




if __name__ == '__main__':
    unittest.main()

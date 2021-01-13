import codon
import unittest


class TestCase1(unittest.TestCase):
    def test2(self):
        cs = []
        for x in range(1000):
            x = codon.random()
            if codon.validcodon(x):
                cs.append(x)
        #print(cs)
        self.assertTrue(len(cs) == 1000)


    def test1(self):
        bases = []
        for x in range(1000):
            b = codon.randombase()
            if codon.validbase(b):
                bases.append(b)
        #print(bases)
        ones = [x for x in bases if x == 1]
        twos = [x for x in bases if x == 2]
        threes = [x for x in bases if x == 3]
        fours = [x for x in bases if x == 4]
        #print(len(ones))
        #print(len(fours))

        self.assertTrue(len(bases) == 1000)
        self.assertTrue(len(ones) > 0)
        self.assertTrue(len(twos) > 0)
        self.assertTrue(len(threes) > 0)
        self.assertTrue(len(fours) > 0)



if __name__ == '__main__':
    unittest.main()

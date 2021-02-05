import asciicode
import myutils
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
        self.assertEqual(asciicode.text_to_binary(protein), "".join([A,C,T,I,N]))

    def test3(self):
        polymer = "LYS-aminoacyl-tRNA synthetase"
        # print(polymer)
        coded = asciicode.text_to_binary(polymer)
        flip = lambda x: myutils.flip_binchar(x) if myutils.random_event(0.001) else x
        num_mutated = 0
        mutation = None
        trials = 1000
        for x in range(0, trials):
            mutated = "".join([ flip(x) for x in coded ])
            if mutated != coded:
                num_mutated += 1
                mutation = mutated
        print("There were %d mutated proteins out of %d trials" %(num_mutated, trials))
        print("Last mutation: %s" %(asciicode.binary_to_text(mutation)))
        # print('orig')
        # print(myutils.printable_at_width(coded, 35))
        # print('last mutation')
        # print(myutils.printable_at_width(mutation, 35))
        diffs = [ i for i in range(len(coded)) if coded[i] != mutation[i] ]
        print("Differences at positions: %s" %(diffs))


    def test4(self):
        coded = asciicode.text_to_binary(protein)
        self.assertEqual(coded, "".join([A,C,T,I,N]))
        decoded = asciicode.binary_to_text(coded)
        self.assertEqual(decoded, protein)


    def test5(self):
        binary = '11000011101101110100111011101101111'
        print("%s is %s" %(binary, asciicode.binary_to_text(binary)))


    def test6(self):
        print("ascii encoding")
        protein = "ALA aminoacyl-tRNA synthetase"
        asciicode.print_with_decoding(protein, 70)


if __name__ == '__main__':
    unittest.main()

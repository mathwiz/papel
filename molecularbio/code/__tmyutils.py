import myutils
import unittest
import random


class TestCase1(unittest.TestCase):
    def test_counter(self):
        count = myutils.counter(4)
        self.assertEqual(next(count), 1)
        self.assertEqual(next(count), 2)
        self.assertEqual(next(count), 3)
        self.assertEqual(next(count), 4)
        with self.assertRaises(StopIteration) as context:
            next(count)


    def test_binary(self):
        self.assertEqual('1', myutils.flip_binchar('0'))
        self.assertEqual('0', myutils.flip_binchar('1'))
        self.assertEqual('0', myutils.flip_binchar('anything'))
   

    def test_random_event(self):
        probability = 0.2
        limit = 100
        count = 0
        for x in range(0, limit):
            if myutils.random_event(probability):
                count += 1
        print(count)
        self.assertTrue(count > 0 and count < limit / 2)


    def test_random_event2(self):
        probability = 0.8
        limit = 100
        count = 0
        for x in range(0, limit):
            if myutils.random_event(probability):
                count += 1
        print(count)
        self.assertTrue(count < limit and count > limit / 2)


    def test_random_event3(self):
        probability = 0.001
        limit = 10000
        count = 0
        for x in range(0, limit):
            if myutils.random_event(probability):
                count += 1
        print(count)
        self.assertTrue(count > 0)



if __name__ == '__main__':
    unittest.main()

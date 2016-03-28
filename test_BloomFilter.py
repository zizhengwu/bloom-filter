from optparse import OptionParser
import unittest
from BloomFilter import *

class TestBloomFilter(unittest.TestCase):
    def test_option_parser(self):
        parser = OptionParser()

        parser.add_option('-N', dest='N', help='size of the universe', type='int', default=100000)
        parser.add_option('-m', dest='m', help='m items into the subset S', type='int', default=10)
        parser.add_option('-n', dest='n', help='the table size of the Bloom filter', type='int', default=500)

        (options, args) = parser.parse_args()

        bloom_filter = BloomFilter(options.N, options.m, options.n)

        self.assertEqual(bloom_filter.N, 100000)
        self.assertEqual(bloom_filter.m, 10)
        self.assertEqual(bloom_filter.n, 500)

    def test_insert_and_check(self):
        parser = OptionParser()

        parser.add_option('-N', dest='N', help='size of the universe', type='int', default=100000)
        parser.add_option('-m', dest='m', help='m items into the subset S', type='int', default=10)
        parser.add_option('-n', dest='n', help='the table size of the Bloom filter', type='int', default=500)

        (options, args) = parser.parse_args()

        bloom_filter = BloomFilter(options.N, options.m, options.n)

        bloom_filter.insert(5)
        self.assertEqual(bloom_filter.check(5), True)
        self.assertEqual(bloom_filter.check(6), False)

if __name__ == '__main__':
    unittest.main()

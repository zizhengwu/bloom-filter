from optparse import OptionParser
from unittest import TestCase
from BloomFilter import *

class TestBloomFilter(TestCase):
    def test_option_parser(self):
        parser = OptionParser()

        parser.add_option('-N', dest='N', help='size of the universe', type='int', default=100000)
        parser.add_option('-m', dest='m', help='m items into the subset S', type='int', default=500)
        parser.add_option('-n', dest='n', help='the table size of the Bloom filter', type='int', default=10)

        (options, args) = parser.parse_args()

        bloom_filter = BloomFilter(options.N, options.m, options.n)

        self.assertEqual(bloom_filter.N, 100000)
        self.assertEqual(bloom_filter.m, 500)
        self.assertEqual(bloom_filter.n, 10)

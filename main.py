from optparse import OptionParser
from BloomFilter import *

def main():
    parser = OptionParser()

    parser.add_option('-N', dest='N', help='size of the universe', type='int', default=100000)
    parser.add_option('-m', dest='m', help='m items into the subset S', type='int', default=10)
    parser.add_option('-n', dest='n', help='the table size of the Bloom filter', type='int', default=500)

    (options, args) = parser.parse_args()

    bloom_filter = BloomFilter(options.N, options.m, options.n)

if __name__ == '__main__':
    main()

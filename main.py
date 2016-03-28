from optparse import OptionParser
from BloomFilter import *
import random

class RunBloomFilter:
    def __init__(self):
        self.bloom_filter = None
        parser = OptionParser()

        parser.add_option('-N', dest='N', help='size of the universe', type='int', default=100000)
        parser.add_option('-m', dest='m', help='m items into the subset S', type='int', default=10)
        parser.add_option('-n', dest='n', help='the table size of the Bloom filter', type='int', default=500)

        (self.options, args) = parser.parse_args()

        print(self.options)

        self.bloom_filter = BloomFilter(self.options.N, self.options.m, self.options.n)

        self.to_be_inserted = random.sample(range(0, self.options.N), self.options.m)
        self.should_be_negative = list(set(range(0, self.options.N)) - set(self.to_be_inserted))

    def insert(self):
        for i in self.to_be_inserted:
            self.bloom_filter.insert(i)

    def check(self):
        correct = 0
        wrong = 0
        for i in self.should_be_negative:
            if self.bloom_filter.check(i) == True:
                wrong += 1
            else:
                correct += 1
        print(wrong / (correct + wrong))

if __name__ == '__main__':
    experiment = RunBloomFilter()
    experiment.insert()
    experiment.check()


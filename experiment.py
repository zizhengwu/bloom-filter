from RunBloomFilter import RunBloomFilter
from optparse import OptionParser
from statistics import mean


if __name__ == '__main__':
    parser = OptionParser()

    parser.add_option('-N', dest='N', help='size of the universe', type='int')
    parser.add_option('-m', dest='m', help='maximum m items into the subset S', type='int')
    parser.add_option('-n', dest='n', help='the table size of the Bloom filter', type='int')
    parser.add_option('-s', dest='s', help='step of items inserted into the subset S', type='int')

    (options, args) = parser.parse_args()

    for i in range(1, options.m, options.s):
        result = []
        for times in range(1, 4):
            arguments = {'n': options.n, 'm': i, 'N': options.N}
            experiment = RunBloomFilter(arguments)
            experiment.insert()
            result.append(experiment.check())
        print('{}\t{}'.format(i, mean(result)))
from RunBloomFilter import RunBloomFilter

if __name__ == '__main__':
    for i in range(1, 50000):
        options = {'n': 65536, 'm': i, 'N': 100000}
        experiment = RunBloomFilter(options)
        experiment.insert()
        print('{}\t{}'.format(i, experiment.check()))
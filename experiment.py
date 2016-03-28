from RunBloomFilter import RunBloomFilter

if __name__ == '__main__':
    for i in range(1, 10000, 5):
        options = {'n': 4096, 'm': i, 'N': 10000}
        experiment = RunBloomFilter(options)
        experiment.insert()
        print('{}\t{}'.format(i, experiment.check()))
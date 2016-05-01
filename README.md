Bloom filters
---

[![Build Status](https://travis-ci.org/zizhengwu/bloom-filters.svg?branch=master)](https://travis-ci.org/zizhengwu/bloom-filters)

# Requirements

- Python 3.5.1

# Results

![Alt text](https://cdn.rawgit.com/zizhengwu/bloom-filters/master/README-static/result.svg)

Not so detailed analysis report available [here](bloom-filters.pdf).

# Run

```
bash run_experiment.sh
```

The script will benchmark the false positive rate of my implementation of Bloom filters regarding different Bloom filter table size and the number of items inserted into the subset that my Bloom filter is maintaining.

The result will be printed to `stdout` and simultaneously piped to `256.txt`, `512.txt`, `1024.txt`, `2048.txt`, and `4096.txt`. Filenames are the sizes of different Bloom filter tables. Inside each file, each line consists of the number of items inserted into the subset that my Bloom filter is maintaining and the false positive rate.

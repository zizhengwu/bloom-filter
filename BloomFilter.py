import math
import random
import unittest


class BloomFilter:
    def __init__(self, N, m, n):
        self.N = N
        self.m = m
        self.n = n
        self.c = self.n / self.m
        self.k = int(self.c * math.log(2))
        self.a = []
        self.b = []
        self.table = dict.fromkeys(list(range(0, self.n)), 0)
        self.create_hash_functions()

    def create_hash_functions(self):
        self.a = random.sample(range(1, self.n), self.k)
        self.b = random.sample(range(1, self.n), self.k)

    def insert(self, x):
        for i in range(0, self.k):
            self.table[(self.a[i] * x + self.b[i]) % self.n] = 1

    def check(self, x):
        for i in range(0, self.k):
            if self.table[(self.a[i] * x + self.b[i]) % self.n] == 0:
                return False
        return True
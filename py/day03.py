from functools import reduce
from operator import and_ as intersect

chunks = lambda I, n: zip(*[iter(I)]*n)

PRIO = {**{chr(ord('a') + v): v+1  for v in range(26)},
        **{chr(ord('A') + v): v+27 for v in range(26)}}

def split(R):
    return [(s[:L], s[L:]) for (s, L) in ((s, len(s)//2) for s in R)]

def day03a(R):
    return sum(PRIO[({*a} & {*b}).pop()] for (a, b) in split(R))

def day03b(R):
    return sum(PRIO[reduce(intersect, C).pop()] for C in chunks(map(set, R), 3))

EX = ['vJrwpWtwJgWrhcsFMMfFFhFp',
      'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
      'PmmdzqPrVvPwwTWBwg',
      'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
      'ttgJtRGJQctTZtZT',
      'CrZsJsPPZsGzwwsLwLmpwMDw']

def test_03_ex1(): assert day03a(EX) == 157
def test_03_ex2(): assert day03b(EX) == 70

def test_03a(day03_lines): assert day03a(day03_lines) == 7863
def test_03b(day03_lines): assert day03b(day03_lines) == 2488
